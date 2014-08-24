from django import forms
from newco.apps.clients.models import Client


class ClientForm(forms.ModelForm):
    """
    Client Forms having name, address and email as fields.
    """
    class Meta:
        model = Client
        fields = ('name', 'email', 'address',)
