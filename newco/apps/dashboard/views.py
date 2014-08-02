from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from django.contrib.auth import views as auth_views
# Create your views here.
from newco import settings


def dashboard(request, *args, **kwargs):
    return render(request, 'dashboard/templates/landing.html')

# Session expires after two weeks
def login(request, *args, **kwargs):

    if request.user.is_authenticated():
        return redirect('dashboard:home')

    if request.method == 'POST':
        if request.POST.get('remember_me', None):
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)

    if request.method == 'GET':
        message = request.GET.get('message', None)
        if message:
            messages.error(request, message)

    return auth_views.login(request, *args, **kwargs)


