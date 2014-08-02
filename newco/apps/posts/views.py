from django.core.urlresolvers import reverse_lazy as reverse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
# Create your views here.
from newco.apps.posts.forms import PostForm
from newco.apps.posts.models import Posts


def add_post(request):
    """
    Add a new post
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, "posts/templates/post_create.html", {'form': form})


class PostListView(ListView):
    model = Posts