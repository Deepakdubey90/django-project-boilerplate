from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from newco.apps.profiles.forms import ProfileForm
from newco.apps.profiles.models import UserProfile


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