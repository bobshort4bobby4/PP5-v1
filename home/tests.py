from django.test import TestCase


from django.test import tag
from django.urls import reverse
from django.contrib.auth.models import User
from stock.models import Vehicle, FuelType, Maker


@tag('views')
class TestHomeViews(TestCase):

    def test_homeview_renders_correct_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_queryset_returns_nothing_if_no_cars_availabletosell(self):
        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m, featured=False, available_sale=False)
        all_stock= Vehicle.objects.all()
        response = self.client.get(reverse('home:home'), kwargs={"Vehicle":all_stock})  
        self.assertEqual(len(response.context["vehicles"]), 0)

    def test_queryset_returns_onevehicle_if_0ne_cars_availabletosell(self):
        m = Maker.objects.create(maker="Bmw")
        f = FuelType.objects.create(fuel="Petrol")
        veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m, featured=True, available_sale=True)
        all_stock= Vehicle.objects.all()
        response = self.client.get(reverse('home:home'), kwargs={"Vehicle": all_stock})  
        self.assertEqual(len(response.context["vehicles"]), 1)