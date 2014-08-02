from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from newco.apps.clients.forms import ClientForm
from newco.apps.clients.models import Client
# Create your views here.




def add_user(request):

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = ClientForm()

    return render(request, "clients/templates/client_create.html", {'form': form})


class ClientListView(ListView):
    model = Client

def deleteuser(request):
    return HttpResponse('This is not so cool')
