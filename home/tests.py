from django.test import TestCase


from django.test import tag
from django.urls import reverse
from django.contrib.auth.models import User


@tag('views')
class TestHomeViews(TestCase):

    def test_homeview_renders_correct_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')