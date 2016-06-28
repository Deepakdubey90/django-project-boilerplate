"""views for clients"""
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from newco.apps.clients.forms import ClientForm
from newco.apps.clients.models import Client
#


class ClientMixin(object):
    """Client Mixin"""
    model = Client

    def get_context_data(self, **kwargs):
        """Setup client object in context"""
        kwargs.update({'object_name': 'Client'})
        return kwargs


class ClientFormMixin(ClientMixin):
    """ Client Form Mixin"""
    form_class = ClientForm
    template_name = 'clients/templates/client_create.html'


class NewClient(FormView):
    form_class = ClientForm
    template_name = 'clients/templates/client_create.html'
    """New Client View"""
    def get_success_url(self):
        return reverse('dashboard:home')


def add_user(request):
    """Add User View Method"""

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

    return render(request, 'clients/templates/client_create.html',
                  {'form': form})


class ClientListView(ListView):
    """List View for Client"""
    model = Client
