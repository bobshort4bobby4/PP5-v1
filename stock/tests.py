"""test for stock app"""
from django.test import TestCase
from django.test import tag
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Vehicle, FuelType, Maker, Tradein
from .trade_calc import calc_tradein


@tag('views')
class TestStockView(TestCase):
    """test for stock app views"""

    def setUp(self):
        """create common variables/instances"""
        User.objects.create_user(
            username='user1',
            password='1234',
            email="mail@mail.com",
            is_staff=False,
        )
        self.client.login(username='user1', password='1234')

        self.m = Maker.objects.create(maker="Bmw")
        self.f = FuelType.objects.create(fuel="Petrol")
        self.veh = Vehicle.objects.create(
                                           stock_num=1,
                                           year="2010",
                                           preowned=True,
                                           price=1000,
                                           odometer=12000,
                                           fuel=self.f,
                                           maker=self.m)
        session = self.client.session
        session['trade_flag'] = False
        session.save()

    def test_delete_vehicle_redirect_to_home_user_notstaff(self):
        """test_delete_vehicle_redirect_to_home_user_notstaff"""

        response = self.client.get(
            reverse('stock:delete_vehicle',
                    kwargs={"vehicle_id": self.veh.stock_num}))
        self.assertEqual(response.status_code, 403)

    def test_delete_vehicle(self):
        """test_delete_vehicle"""

        User.objects.create_user(
            username='user2',
            password='1234',
            email="mail@mail.com",
            is_staff=True,
        )
        self.client.login(username='user2', password='1234')

        session = self.client.session
        session['trade_flag'] = False
        session.save()

        response = self.client.post(
            reverse('stock:delete_vehicle',
                    kwargs={"vehicle_id": self.veh.stock_num}))
        avsaleveh = Vehicle.objects.all()
        self.assertEqual(len(avsaleveh), 0)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))

    def test_edit_vehicle_redirect_to_home_user_notstaff(self):
        """test_edit_vehicle_redirect_to_home_user_notstaff"""

        response = self.client.get(
            reverse('stock:edit_vehicle',
                    kwargs={"vehicle_id": self.veh.stock_num}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Sorry, only store staff can do that.')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))

    def test_edit_vehicle_displays_correct_message_if_invalid_form(self):
        """test_edit_vehicle_displays_correct_message_if_invalid_form"""

        User.objects.create_user(
                                username='user2',
                                password='1234',
                                email="mail@mail.com",
                                is_staff=True,
                                )

        self.client.login(username='user2', password='1234')

        session = self.client.session
        session['trade_flag'] = False
        session.save()

        response = self.client.post(
            reverse('stock:edit_vehicle',
                    kwargs={"vehicle_id": self.veh.stock_num}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to update Vehicle. '
                         'Please ensure the form is valid.')

    def test_StockView_renders_correct_template_if_q_empty(self):
        """test_StockView_renders_correct_template_if_q_empty"""

        response = self.client.get(reverse('stock:stock'), {"q": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "You didn't enter any search criteria!")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/stock.html')

    def test_clear_trade_works(self):
        trade_details = {
                 'manufacturer': "Bmw",
                 'model': "3 series",
                 'year': "2000",
                 'odo': "12000",
                 'condition': "1",
                 'trade_value': 20000,
                 'full_price': "25000"
         }

        session = self.client.session
        session['trade_flag'] = True
        session['trade_details'] = trade_details
        session.save()
        response = self.client.get(reverse('stock:clear_trade'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Cleared Trade-ins")
        self.assertRedirects(response, reverse('stock:trade_in'))
        session = self.client.session
        self.assertFalse(session['trade_flag'])

    def test_trade_calc_function_returning_correct_values(self):
        """ tests ouput from calc_tradein
            Inputs:
                manu; string 'Ford'
                year; string "2015'
                model; string 'ka'
                odo; string '20000'
                condition; string '1'

            Expected output:
            trade_val == 12994
            full_price == 19491
        """
        Maker.objects.create(maker="Ford", base_price=25000)
        manu = "Ford"
        manu = get_object_or_404(Maker, maker=manu)
        year = "2015"
        odo = "20000"
        condition = "3"
        trade_val, full_price = calc_tradein(manu, year, odo, condition)

        self.assertEqual(trade_val, 12994)
        self.assertEqual(full_price, 19491)


@tag("models")
class TestModels(TestCase):
    """test models for stock app"""

    def setUp(self):
        """define common variables/instances"""

        self.m = Maker.objects.create(maker="Bmw")
        self.f = FuelType.objects.create(fuel="Petrol")
        self.veh = Vehicle.objects.create(
                                        stock_num=1,
                                        model="3 series",
                                        year="2010",
                                        preowned=True,
                                        price=1000,
                                        odometer=12000,
                                        fuel=self.f,
                                        maker=self.m)

    def test_models_stringmethods_returns_correctstring(self):
        """test_models_stringmethods_returns_correctstring"""

        self.assertEqual(str(self.veh), 'Bmw, 3 series')
        self.assertEqual(str(self.m), "Bmw")
        self.assertEqual(str(self.f), "Petrol")

    def test_TradeIn_model_sring_method(self):
        tradeinitem = Tradein.objects.create(user="testuser",
                                             manufacturer="Ford",
                                             mod="ka",
                                             odo="12000",
                                             condition="1",
                                             year="2010",
                                             trade_value=10000,
                                             full_price=12000,)

        self.assertEqual(
            str(tradeinitem),
            f'{tradeinitem.manufacturer} {tradeinitem.mod}'
            f' value {tradeinitem.trade_value}')
