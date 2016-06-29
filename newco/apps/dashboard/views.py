"""Views for Dashboard app"""
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import views as auth_views
# Create your views here.
from newco import settings
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

def home(request):
    """view for dashboard for landing page"""
    if not request.user.is_authenticated():
        return redirect(reverse('dashboard:login'))
    return render(request, 'dashboard/templates/landing.html')