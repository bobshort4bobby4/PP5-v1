from django.test import TestCase
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
import datetime


@tag("views")
class TestChecckoutViews(TestCase):

    def test_checkout_success_render_correct_template(self):

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
        response = self.client.get(reverse('checkout:checkout_success', kwargs={"order_number":ord.order_number}))
        messages = list(get_messages(response.wsgi_request))     
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Order successfully processed! \
        Your order number is {ord.order_number}. A confirmation \
        email will be sent to {ord.email}.')
        self.assertEqual(response.status_code, 200)
      
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    

    def test_checkout_success_attachs_profile_if_user(self):
        pro =UserProfile.objects.all()
        
        self.assertEqual(len(pro), 0)
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
        
        user1 = User.objects.create_user(        
                                    username='user1',
                                    password='1234',
                                    email="mail@mail.com",
                                    is_staff=True,
                            )
        self.client.login(username='user1', password='1234')

        session = self.client.session
        session['save_info'] = True
        session.save()
        response = self.client.get(reverse('checkout:checkout_success', kwargs={"order_number":ord.order_number}))
        
        pro =UserProfile.objects.all()
        self.assertEqual(len(pro), 1)

    def test_checkout_get_redirects_if_bag_empty(self):
        response = self.client.get(reverse('checkout:checkout'), follow=True) 
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "There's nothing in your bag at the moment")
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('stock:stock'))

    def test_checkout_get_renders_correct_template(self):
        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
        session = self.client.session
        session['bag'] = "1"
        session.save()
        response = self.client.get(reverse('checkout:checkout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')