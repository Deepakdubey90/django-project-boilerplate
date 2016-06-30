"""views for clients"""
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from newco.apps.clients.models import Client


class NewClient(CreateView):
    model = Client
    fields = ['name', 'email', 'address']

    def get_success_url(self):
        return reverse('dashboard:home')


class ClientListView(ListView):
    """List View for Client"""
    # template_name = 'clients/templates/client_list.html'
    model = Client
