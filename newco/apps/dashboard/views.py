"""Views for Dashboard app"""
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def home(request):
    """view for dashboard for landing page"""
    if not request.user.is_authenticated():
        return redirect(reverse('dashboard:login'))
    return render(request, 'dashboard/templates/landing.html')
