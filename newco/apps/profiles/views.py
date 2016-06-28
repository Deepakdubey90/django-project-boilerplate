"""views for profiles app"""
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, FormView
from newco.apps.profiles.forms import ProfileForm
from newco.apps.profiles.models import UserProfile

class NewProfile(FormView):
    """new profile view"""
    form_class = ProfileForm
    template_name = 'profiles/templates/profile_create.html'

    def get_success_url(self):
        return reverse('dashboard:home')


def add_profile(request):
    """add profile view function"""
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, "profiles/templates/profile_create.html",
                  {'form': form})

class ProfileList(ListView):
    """Profile List View"""
    model = UserProfile

