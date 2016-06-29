from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import UserProfile
from newco.apps.clients.models import Client


class ProfilesCreateTestCase(TestCase):
    def test_profile_create(self):
        client1 = Client.objects.create(name='test user1', email='test@example.com', address='example address')
        resp = self.client.post(reverse('profiles:profile_create'),
                                data={
                                    'profile_user': client1,
                                    'info': True,
                                    'status': 'Single'
                                })
        self.assertEqual(resp.status_code, 200)


class ProfilesListTestCase(TestCase):
    def setUp(self):
        client1 = Client.objects.create(name='test user1', email='test@example.com', address='example address')
        client2 = Client.objects.create(name='test user2', email='test2@example.com', address='example address')
        UserProfile.objects.create(profile_user=client1, info='True', status='single')
        UserProfile.objects.create(profile_user=client2, info='True', status='married')

    def test_profiles(self):
        resp = self.client.get(reverse('profiles:list_profiles'))
        self.assertContains(resp, 'single')
        self.assertContains(resp, 'married')

