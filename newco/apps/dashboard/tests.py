from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your tests here.

class DashboardPageTestCase(TestCase):
    def test_home_page(self):
        resp = self.client.get(reverse('dashboard:home'))
        self.assertEqual(resp.status_code, 302)


class DashboardLoginTestCase(TestCase):
    def test_login(self):
        User.objects.create_user(username='vinit', password='linux')
        resp = self.client.post(reverse('dashboard:login'),
                                data={'username': 'root', 'password': 'linux'})
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(reverse('dashboard:login'),
                                data={'username': 'vinit', 'password': 'linux'})
        self.assertEqual(resp.status_code, 302)
