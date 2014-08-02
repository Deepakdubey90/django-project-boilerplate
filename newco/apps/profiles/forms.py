from django import forms
from newco.apps.profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_user', 'picture', 'info', 'status')