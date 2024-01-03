from django.test import TestCase, RequestFactory
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from .views import index, about, my_view


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name='John', last_name='Doe', email='john@example.com', gender='M')

    def test_customer_name(self):
        customer = Customer.objects.get(first_name='John')
        self.assertEqual(customer.first_name, 'John')


class CustomerFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com'
        }
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'john@example.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_widgets(self):
        form = CustomerForm()
        self.assertIn('class="form-control"', str(form['first_name']))
        self.assertIn('class="form-control"', str(form['last_name']))
        self.assertIn('class="form-control"', str(form['email']))


# class ViewsTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#
#     def test_index_view(self):
#         url = reverse('index')
#         request = self.factory.get(url)
#         response = index(request)
#         self.assertEqual(response.status_code, 200)
#
#     def test_about_view_get(self):
#         url = reverse('about')
#         request = self.factory.get(url)
#         response = about(request)
#         self.assertEqual(response.status_code, 200)
#
#     def test_about_view_post_valid_form(self):
#         url = reverse('about')
#         data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'email': 'john@example.com',
#             'gender': 'M'
#         }
#         request = self.factory.post(url, data=data)
#         response = about(request)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertRedirects(response, '/')  # Check the redirect destination
#
#     def test_about_view_post_invalid_form(self):
#         url = reverse('about')
#         data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'email': 'invalid_email',  # Invalid email format
#             'gender': 'M'
#         }
#         request = self.factory.post(url, data=data)
#         response = about(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'KUDINOV/auto.html')
#         self.assertContains(response, 'Форма была неверной')  # Check for error message in the response
#
#     def test_my_view(self):
#         url = reverse('my_view')
#         request = self.factory.get(url)
#         response = my_view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('related_products', response.context)  # Check if the context variable exists
#
#         related_products = response.context['related_products']
#         self.assertQuerysetEqual(related_products, ['<Product: Product 1>', '<Product: Product 2>'])
