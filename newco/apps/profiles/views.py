"""views for profiles app"""
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from newco.apps.profiles.models import UserProfile


class NewProfile(CreateView):
    """new profile view"""
    model = UserProfile
    fields = ['profile_user', 'picture', 'status', 'info']

    def get_success_url(self):
        return reverse('dashboard:home')


class ProfileList(ListView):
    """Profile List View"""
    model = UserProfile

