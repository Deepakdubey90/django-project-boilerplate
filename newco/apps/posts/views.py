from django.core.urlresolvers import reverse_lazy as reverse
from django.shortcuts import render, redirect
from django.views.generic import FormView
# Create your views here.
from newco.apps.posts.forms import PostForm
from newco.apps.posts.models import Posts


class PostFormView(FormView):
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def setup(self):
        pass

    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        tags = form.cleaned_data['tags']
        post_object = Posts(title=title, content=content, tags=tags)
        post_object.save()
        return super(PostFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:home')



def add_post(request):

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