from django.contrib import admin
from newco.apps.posts.models import Posts
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user',)
    list_filter = ('user', 'title',)

admin.site.register(Posts, PostAdmin)