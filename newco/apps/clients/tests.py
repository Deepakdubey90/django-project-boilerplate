from django.test import TestCase
from .models import Client


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='test user1', email='test@example.com', address='example address')

    def test_clients_are_created(self):
        client1 = Client.objects.get(name='test user1')
        self.assertEqual(client1.id, 2)
