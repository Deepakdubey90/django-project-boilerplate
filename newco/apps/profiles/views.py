"""views for profiles app"""
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView
from newco.apps.profiles.forms import ProfileForm
from newco.apps.profiles.models import UserProfile


class NewProfile(CreateView):
    """new profile view"""
    model = UserProfile
    fields = ['profile_user', 'picture', 'status', 'info']

    # template_name = 'profiles/templates/profile_create.html'

    def get_success_url(self):
        return reverse('dashboard:home')


class ProfileList(ListView):
    """Profile List View"""
    model = UserProfile

