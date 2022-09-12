# from django.test import TestCase
# from django.test import tag
# from django.urls import reverse
# from django.http import HttpRequest
# from django.contrib.messages import get_messages
# from django.test import tag
# from django.contrib.auth.models import User
# from .models import Vehicle, FuelType, Maker
# from .forms import VehicleForm


# @tag('views')
# class TestStockView(TestCase):

#     def test_StockView_renders_correct_template(self):
#         response = self.client.get(reverse('stock:stock'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'stock/stock.html')


#     def test_StockDetail_renders_correct_template(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.get(reverse('stock:stock_detail', kwargs={"pk":veh.stock_num}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'stock/stock_detail.html')


#     def test_Edit_Delete_View_renders_correct_template(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.get(reverse('stock:edit_delete', kwargs={"stock_num":veh.stock_num}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'stock/edit_delete.html')


#     def test_delete_vehicle_redirect_to_home_user_notstaff(self):
#         user1 = User.objects.create_user(
#             username='user1',
#             password='1234',
#             email="mail@mail.com",
#             is_staff=False,
#         )
#         self.client.login(username='user1', password='1234')

#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.get(reverse('stock:delete_vehicle', kwargs={"vehicle_id":veh.stock_num}))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'Sorry, only store staff can do that.')

#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('home:home'))


#     def test_delete_vehicle(self):
#         user1 = User.objects.create_user(
#             username='user1',
#             password='1234',
#             email="mail@mail.com",
#             is_staff=True,
#         )
#         self.client.login(username='user1', password='1234')

#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, year="2010",available_sale=True, preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.post(reverse('stock:delete_vehicle', kwargs={"vehicle_id":veh.stock_num}))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'Vehicle Deleted!')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('stock:stock'))


#     def test_edit_vehicle_redirect_to_home_user_notstaff(self):
#         user1 = User.objects.create_user(
#             username='user1',
#             password='1234',
#             email="mail@mail.com",
#             is_staff=False,
#         )
#         self.client.login(username='user1', password='1234')

#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         veh = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         response = self.client.get(reverse('stock:edit_vehicle', kwargs={"vehicle_id":veh.stock_num}))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'Sorry, only store staff can do that.')

#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('home:home'))


#     def test_edit_vehicle_displays_correct_message_if_invalid_form(self):

#         user1 = User.objects.create_user(
#                                 username='user1',
#                                 password='1234',
#                                 email="mail@mail.com",
#                                 is_staff=True,
#                                 )

#         self.client.login(username='user1', password='1234')

#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         ve = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         form = VehicleForm()
#         response = self.client.post(reverse('stock:edit_vehicle', kwargs={"vehicle_id":ve.stock_num}))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'Failed to update Vehicle. '
#                                              'Please ensure the form is valid.')

#     def test_StockView_renders_correct_template_if_q_null(self):
#         response = self.client.get(reverse('stock:stock'), {"q": ""})
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "You didn't enter any search criteria!")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'stock/stock.html')























# #      def test_edit_vehicle_displays_correct_message_if_invalid_form(self):

# #         user1 = User.objects.create_user(
# #                                 username='user1',
# #                                 password='1234',
# #                                 email="mail@mail.com",
# #                                 is_staff=True,
# #                                 )

# #         self.client.login(username='user1', password='1234')

# #         m = Maker.objects.create(maker="Bmw")
# #         f = FuelType.objects.create(fuel="Petrol")
# #         veh = Vehicle.objects.create(stock_num=1, year="2010", model="cartest", preowned=True, price=1000, odometer=12000, fuel=f, maker=m, featured=True, colour="testcolour", available_sale=True )
        
# #         # request = HttpRequest()
# #         data = {
# #             "stock_num": 1,
# #             "maker": m,
# #             "model": "cartest",
# #             "year": "2011",
# #             "fuel": f,
# #             "featured": True,
# #             "preowned": True,
# #             "price": 1000,
# #             "odometer": 12000,
# #             "colour": "testcolour",
# #             "available_sale": True,
# #         }

        
# #         form = VehicleForm(data)
# #         data = form.initial 
# #         data['year'] = '2011'
# #         response = self.client.post(reverse('stock:edit_vehicle', kwargs={"vehicle_id":veh.stock_num}), data)
# #         form = response.context['form']
# #         # form is unbound but contains data

# # # manipulate some data
        
       
# #         # messages = list(get_messages(response.wsgi_request))
# #         # form.save()
        
# #         veh = Vehicle.objects.get(pk=1)
# #         print(Vehicle.objects.count())
# #         self.assertTrue(form.is_valid())
# @tag('forms')
# class TestVehicleForm(TestCase):

#     def test_all_required_fields_are_required(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         ve = Vehicle.objects.create(stock_num=1, year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         form = VehicleForm({
#                         "stock_num": ve.stock_num,
#                         "maker": m,
#                         "model": "cartest",
#                         "year": "2011",
#                         "fuel": f,
#                         "featured": True,
#                         "preowned": True,
#                         "price": 1000,
#                         "odometer": 10000,
#                         "colour": "white",
#                         "available_sale": True,
#          })

#         self.assertTrue(form.is_valid())

#         form = VehicleForm({
#                         "stock_num": 1,
#                         "maker": m,
#                         "model": "",
#                         "fuel": f,
#                         "featured": True,
#                         "preowned": True,
#                         "price": 1000,
#                         "odometer": 10000,
#                         "colour": "white",
#                         "available_sale": True,
#         })

#         self.assertFalse(form.is_valid())


# @tag("models")
# class TestModels(TestCase):

#     def test_models_stringmethods_returns_correctstring(self):
#         m = Maker.objects.create(maker="Bmw")
#         f = FuelType.objects.create(fuel="Petrol")
#         ve = Vehicle.objects.create(stock_num=1, model="3 series", year="2010", preowned=True, price=1000, odometer=12000, fuel=f, maker=m)
#         self.assertEqual(str(ve), 'Bmw, 3 series')
#         self.assertEqual(str(m), "Bmw")
#         self.assertEqual(str(f), "Petrol")
