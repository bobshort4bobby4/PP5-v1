from django.test import TestCase

import json
from django.shortcuts import get_object_or_404
import datetime
from django.test import tag
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.messages import get_messages
from django.test import tag
from django.contrib.auth.models import User
from stock.models import Vehicle, FuelType, Maker
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from.models import Order, OrderLineItem


@tag("models")
class TestCheckoutModels(TestCase):

    def test_order_stribn_method_works(self):
        orderitem = Order.objects.create(
                                    user_profile=None,
                                    full_name='Robert',
                                    email='ma@mail.com',
                                    country='BS',
                                    phone_number="1234",
                                    postcode='1234',
                                    town_or_city='12345',
                                    street_address1='45',
                                    street_address2='45',
                                    county='45687',
                                    date=datetime.datetime(2022, 9, 13, 14, 11, 35),
                                    delivery_cost=0,
                                    order_total=0,
                                    grand_total=0,
                                    original_bag="",
                                    stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj'
                            )


        self.assertEqual(str(orderitem), orderitem.order_number) 

    def test_OrderLineItem_string_method_works(self):
        orderitem = Order.objects.create(
                                    user_profile=None,
                                    full_name='Robert',
                                    email='ma@mail.com',
                                    country='BS',
                                    phone_number="1234",
                                    postcode='1234',
                                    town_or_city='12345',
                                    street_address1='45',
                                    street_address2='45',
                                    county='45687',
                                    date=datetime.datetime(2022, 9, 13, 14, 11, 35),
                                    delivery_cost=0,
                                    order_total=0,
                                    grand_total=0,
                                    original_bag="",
                                    stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj'
                            )

        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
        orderlineitem = OrderLineItem.objects.create(order=orderitem, product=veh, quantity=1)
        self.assertEqual(str(orderlineitem), f'Vehicle No. {orderlineitem.product.stock_num} \
                             on order {orderlineitem.order.order_number}') 




@tag("views")
class TestCheckoutViews(TestCase):


    def test_checkoutsuccess_render_correct_template(self):
        session = self.client.session
        session['trade_flag'] = False
        session.save()
        ord = Order.objects.create(user_profile=None,
                                   full_name='Robert',
                                   email='ma@mail.com',
                                   country='BS',
                                   phone_number="1234",
                                   postcode='1234',
                                   town_or_city='12345',
                                   street_address1='45',
                                   street_address2='45',
                                   county='45687',
                                   date=datetime.datetime(2022,
                                                          9,
                                                          13,
                                                          14,
                                                          11,
                                                          35),
                                   delivery_cost=0,
                                   order_total=0,
                                   grand_total=0,
                                   original_bag="",
                                   stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj',)


        response = self.client.get(reverse('checkout:checkout_success', kwargs={"order_number":ord.order_number}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Order successfully processed! \
        Your order number is {ord.order_number}. A confirmation \
        email will be sent to {ord.email}.')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


    def test_checkout_success_attachs_profile_if_user(self):
        user1 = User.objects.create_user(        
                                    username='user1',
                                    password='1234',
                                    email="mail@mail.com",
                                    is_staff=True,
                            )
        self.client.login(username='user1', password='1234')
        session = self.client.session
        session['trade_flag'] = False
        session.save()

        ord = Order.objects.create(
                                    user_profile=None,
                                    full_name='Robert',
                                    email='ma@mail.com',
                                    country='BS',
                                    phone_number="1234",
                                    postcode='1234',
                                    town_or_city='12345',
                                    street_address1='45',
                                    street_address2='45',
                                    county='45687',
                                    date=datetime.datetime(2022, 9, 13, 14, 11, 35),
                                    delivery_cost=0,
                                    order_total=0,
                                    grand_total=0,
                                    original_bag="",
                                    stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj'
                            )


        pro =UserProfile.objects.all()
        self.assertEqual(len(pro), 1)
        response = self.client.get(reverse('checkout:checkout_success', kwargs={"order_number":ord.order_number} ))
        neworder= get_object_or_404(Order, pk=1)
        self.assertEqual(neworder.user_profile.user.username, "user1")


    def test_checkoutsuccess_resets_session_variables(self):
        user1 = User.objects.create_user(        
                                    username='user1',
                                    password='1234',
                                    email="mail@mail.com",
                                    is_staff=True,
                            )
        self.client.login(username='user1', password='1234')
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
        session['bag'] = "1"
        session['trade_details'] = trade_details
        session.save()

        ord = Order.objects.create(
                                    user_profile=None,
                                    full_name='Robert',
                                    email='ma@mail.com',
                                    country='BS',
                                    phone_number="1234",
                                    postcode='1234',
                                    town_or_city='12345',
                                    street_address1='45',
                                    street_address2='45',
                                    county='45687',
                                    date=datetime.datetime(2022, 9, 13, 14, 11, 35),
                                    delivery_cost=0,
                                    order_total=0,
                                    grand_total=0,
                                    original_bag="",
                                    stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj'
                            )
            
        response = self.client.get(reverse('checkout:checkout_success', kwargs={"order_number":ord.order_number} ))
        session = self.client.session
        if 'bag' in session:
            newbag = True
        else:
            newbag = False
        
        self.assertFalse(newbag)
        self.assertFalse(session['trade_flag'])
        self.assertEqual(session['trade_details']['trade_value'], 0)







    def test_checkout_get_redirects_if_bag_empty(self):
        session = self.client.session
        session['trade_flag'] = False
        session.save()
        response = self.client.get(reverse('checkout:checkout'), follow=True) 
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "There's nothing in your bag at the moment")
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('stock:stock'))

    def test_checkout_get_renders_correct_template(self):
        session = self.client.session
        session['trade_flag'] = False
        session.save()
        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
        session = self.client.session
        session['bag'] = "1"
        session.save()
        response = self.client.get(reverse('checkout:checkout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_post_renders_correct_template(self):
        session = self.client.session
        session['trade_flag'] = False
        session['bag'] = "1"
        session.save()
        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1,
                                     year="2010",
                                     preowned=True,
                                     price=1000,
                                     odometer=12000,
                                     fuel=f,
                                     maker=m)

        response = self.client.post(reverse('checkout:checkout'),
                                    {"full_name": 'testuser',
                                    "email": 'me@mail.com',
                                     "phone_number": '123456',
                                     "country": "BE",
                                     "postcode": "asd123",
                                     "town_or_city": 'dublin',
                                     "street_address1": 'here',
                                     "street_address2": 'there',
                                     "county": 'anywhere',
                                     "client_secret": '1234567890qwertyudf'},
                                    follow=True)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')                                  
