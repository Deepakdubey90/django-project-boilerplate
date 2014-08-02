from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView
from newco.apps.profiles.forms import ProfileForm
from newco.apps.profiles.models import UserProfile


class ProfileMixin(object):
    model = UserProfile
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'UserProfile'})
        return kwargs


class ProfileFormMixin(ProfileMixin):
    form_class = ProfileForm
    template_name = 'profiles/templates/profile_create.html'


class NewProfile(ProfileFormMixin, CreateView):
    def get_success_url(self):
        return reverse('dashboard:home')


def add_profile(request):
    """
    Add new profile
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, "profiles/templates/profile_create.html", {'form': form})

class ProfileList(ListView):
    model = UserProfile