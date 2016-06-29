from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

class DashboardPageTestCase(TestCase):
    def test_home_page(self):
        resp = self.client.get(reverse('dashboard:home'))
        self.assertEqual(resp.status_code, 200)


class DashboardLoginTestCase(TestCase):
    def test_login(self):
        pass