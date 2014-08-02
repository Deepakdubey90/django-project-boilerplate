from django.shortcuts import render

# Create your views here.

def dashboard(request, *args, **kwargs):
    return render(request, 'dashboard/templates/landing.html')