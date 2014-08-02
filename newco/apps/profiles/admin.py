from django.contrib import admin

# Register your models here.
from newco.apps.profiles.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_user', 'status')

admin.site.register(UserProfile, UserProfileAdmin)