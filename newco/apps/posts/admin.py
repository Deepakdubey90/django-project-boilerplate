from django.contrib import admin
from newco.apps.posts.models import Posts


class PostAdmin(admin.ModelAdmin):
    """
    Post admin
    """
    list_display = ('title', 'content', 'user',)
    list_filter = ('user', 'title',)

admin.site.register(Posts, PostAdmin)