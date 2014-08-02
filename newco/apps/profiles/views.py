from django.shortcuts import render, redirect

# Create your views here.
from newco.apps.profiles.forms import ProfileForm


def add_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = ProfileForm()

    return render(request, "profiles/templates/profile_create.html", {'form': form})