from urllib import response
import django
from django.test import Client, TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from app import views


# Views take a web request and return a web response


class TestViews(TestCase):
    # tests for the application views
    @classmethod
    def setUp(self):
        client = Client()

    def test_home_URL_exists_at_desired_location(self):
        web_response = self.client.get('/home/')
        self.assertEqual(web_response.status_code, 200)

    def test_home_url_accessable_by_name(self):
        web_response = self.client.get(reverse('home'))
        self.assertEqual(web_response.status_code, 200)

    def test_home_uses_correct_template(self):
        web_response = self.client.get(reverse('home'))
        self.assertEqual(web_response.status_code, 200)
        self.assertTemplateUsed(web_response, 'home.html')

    # ________________________________________________________________

    def test_contact_URL_exists_at_desired_location(self):
        web_response = self.client.get('/contact/')
        self.assertEqual(web_response.status_code, 200)

    def test_contact_url_accessable_by_name(self):
        web_response = self.client.get(reverse('contact'))
        self.assertEqual(web_response.status_code, 200)

    def test_contact_uses_correct_template(self):
        web_response = self.client.get(reverse('contact'))
        self.assertEqual(web_response.status_code, 200)
        self.assertTemplateUsed(web_response, 'contact.html')

    # ________________________________________________________________

    def test_overview_URL_exists_at_desired_location(self):
        web_response = self.client.get('/overview/')
        self.assertEqual(web_response.status_code, 200)

    def test_overview_url_accessable_by_name(self):
        web_response = self.client.get(reverse('overview'))
        self.assertEqual(web_response.status_code, 200)

    def test_overview_uses_correct_template(self):
        web_response = self.client.get(reverse('overview'))
        self.assertEqual(web_response.status_code, 200)
        self.assertTemplateUsed(web_response, 'overview.html')

    # ______________________________________________________________

    def test_details_URL_exists_at_desired_location(self):
        web_response = self.client.get('/details/')
        self.assertEqual(web_response.status_code, 200)

    def test_details_url_accessible_by_name(self):
        web_response = self.client.get(reverse('details'))
        self.assertEqual(web_response.status_code, 200)

    def test_details_use_correct_template(self):
        web_response = self.client.get(reverse('details'))
        self.assertEqual(web_response.status_code, 200)
        self.assertTemplateUsed(web_response, 'details.html')

    # _______________________________________________________________

    def test_login_URL_exists_at_desired_location(self):
        web_response = self.client.get('/login/')
        self.assertEqual(web_response.status_code, 200)

    def test_login_url_accessible_by_name(self):
        web_response = self.client.get(reverse('login'))
        self.assertEqual(web_response.status_code, 200)

    def test_login_use_correct_template(self):
        web_response = self.client.get(reverse('login'))
        self.assertEqual(web_response.status_code, 200)
        self.assertTemplateUsed(web_response, 'login.html')
