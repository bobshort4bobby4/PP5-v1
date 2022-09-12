# from django.test import TestCase
# from django.test import tag
# from django.urls import reverse
# from django.contrib.messages import get_messages
# from stock.models import Maker, FuelType, Vehicle


# @tag("views")
# class TestBagViews(TestCase):

#     def test_add_to_bag_redirect_correctly_if_vehicle_in_bag_already(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, model="3 series", year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         session = self.client.session
#         session['bag'] = "1"
#         session.save()
#         response = self.client.post(reverse('bag:add_to_bag', kwargs={"item_id":veh.stock_num}), follow=True)
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), f'This Vehicle  {veh.maker} {veh.model} \
#                          is already in your bag')
#         self.assertRedirects(response, reverse('stock:stock'))
#         self.assertEqual(response.status_code, 200)

#     def test_add_to_bag_correctly_adds_vehicle(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, model="3 series", year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.post(reverse('bag:add_to_bag', kwargs={"item_id":veh.stock_num}), follow=True)
#         session = self.client.session["bag"]
#         self.assertEqual(len(session), 1)
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), f'Added {veh.maker} {veh.model} to your bag')
#         self.assertRedirects(response, reverse('stock:stock'))
#         self.assertEqual(response.status_code, 200)

#     def test_remove_from_bag_works_and_redirects(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, model="3 series", year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         session = self.client.session
#         session['bag'] = "1"
#         session.save()
        
#         response = self.client.post(reverse('bag:remove_from_bag', kwargs={"item_id":veh.stock_num}), follow=True)
#         session = self.client.session["bag"]
#         self.assertEqual(len(session), 0)
#         self.assertRedirects(response, reverse("bag:bag"))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), f'Removed {veh.maker} {veh.model} from your bag')
        
