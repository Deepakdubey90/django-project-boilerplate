from django.http import HttpResponse
from django.shortcuts import render
from newco.apps.clients.models import Client
# Create your views here.

def adduser(request):
    return HttpResponse('This is so cool')


def deleteuser(request):
    return HttpResponse('This is not so cool')
