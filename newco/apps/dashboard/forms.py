from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    Email is used as default username.
    """
    username = forms.CharField(max_length=254, label=_("Username or e-mail"),
                                widget=forms.TextInput(attrs={'class': 'form-control input-login',
                                'placeholder': _("Username"), 'required': 'required'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(
                                attrs={'class': 'form-control input-login',
                                'placeholder': _("Password"), 'required': 'required'}))

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s or Email and password. "
                           "Note that password is case-sensitive."),
        'inactive': _("This account is inactive."),
    }
