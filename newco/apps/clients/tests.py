from django.test import TestCase
from .models import Client
from django.core.urlresolvers import reverse



class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='test user1', email='test@example.com', address='example address')

    def test_clients_are_created(self):
        client1 = Client.objects.get(name='test user1')
        self.assertEqual(client1.name, 'test user1')

class ClientListTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='test user1', email='test@example.com', address='example address')
        Client.objects.create(name='test user2', email='test@example.com',
                address='eadxample address')

    def test_clients_are_created(self):
        resp = self.client.get(reverse('clients:list_users'))
        self.assertContains(resp, 'test user1')
        self.assertContains(resp, 'test user2')
