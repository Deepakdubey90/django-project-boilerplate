from django.test import TestCase
from .models import Posts
from newco.apps.clients.models import Client


class PostTestCase(TestCase):

    def setUp(self):
        Client.objects.create(name='new user', email='new@gmail.com',
                              address='new address')
        Posts.objects.create(title='New Post', content='Dummy content',
                             user=Client.objects.get(name='new user'))

    def test_post_creation(self):
        """
        Test if posts are created.
        """
        client1 = Client.objects.get(name='new user')
        post = Posts.objects.get(user=client1)
        # a post would only be created if it has the id, in this case 1
        self.assertEqual(post.id, 1)

