from django.test import TestCase

"""tests for profile app"""
import datetime
from django.test import tag
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.contrib.messages import get_messages


@tag('views')
class TestProfileViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
                                username='user1',
                                password='1234',
                                email="mail@mail.com",
                                is_staff=True,
                                )

        self.client.login(username='user1', password='1234')

        session = self.client.session
        session['trade_flag'] = False
        session.save()

    def test_profile_uses_correct_template(self):

        """test_profile_uses_correct_template"""

        response = self.client.post(reverse('profiles:profile'))
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history_uses_correct_template(self):
        """test_order_history_uses_correct_template"""

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
                                    date=datetime.datetime(2022,
                                                           9, 13, 14, 11, 35),
                                    delivery_cost=0,
                                    order_total=0,
                                    grand_total=0,
                                    original_bag="",
                                    stripe_pid='pi_3LhZpDCzyNbeBsFO0zmNolVj'
                            )
        response = self.client.get(
            reverse('profiles:order_history',
                    kwargs={"order_number": ord.order_number}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            f'This is a past confirmation for order number {ord.order_number}.'
            ' A confirmation email was sent on the order date.')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


@tag('forms')
class TestProfilesForms(TestCase):
    def test_string_method_for_profile_models(self):
        """test_string_method_for_profile_models"""

        User.objects.create_user(
                                username='user1',
                                password='1234',
                                email="mail@mail.com",
                                is_staff=True,
                                )
        testuser = get_object_or_404(UserProfile, pk=1)
        self.assertEqual(str(testuser), 'user1')
