from django.test import TestCase
from django.core.urlresolvers import reverse_lazy as reverse
from newco.apps.posts.models import Posts
from newco.apps.clients.models import Client


class PostCreateTestCase(TestCase):

    def test_post_creation(self):
        """
        Test if posts are created.
        """
        client = Client.objects.create(name='test user1',
                                       email='test@example.com',
                                       address='example address')
        resp = self.client.post(reverse('posts:post_create'),
                                data={'title': 'Yo',
                                      'content': 'done',
                                      'user': client})
        self.assertEqual(resp.status_code, 200)



class PostListTestCase(TestCase):

    def test_post_list_creation(self):
        """
        Test if posts are created.
        """
        client = Client.objects.create(name='test user1',
                                       email='test@example.com',
                                       address='example address')
        Posts.objects.create(title='Yo', content='done', user=client)
        Posts.objects.create(title='Go', content='done', user=client)
        resp = self.client.get(reverse('posts:list_posts'))
        self.assertContains(resp, 'Yo')
        self.assertContains(resp, 'Go')
        self.assertEqual(resp.status_code, 200)
