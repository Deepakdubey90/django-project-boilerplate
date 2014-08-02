from django import forms
from newco.apps.clients.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'address',)