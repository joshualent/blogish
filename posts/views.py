from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

# Create your views here.


class PostListView(ListView):
    """Post List View"""

    template_name = "posts/post_list.html"
    model = Post


class PostDetailView(DetailView):
    """Post List View"""

    template_name = "posts/post_detail.html"
    model = Post


class PostCreateView(CreateView):
    """Post Create View"""

    template_name = "posts/post_new.html"
    model = Post
    fields = ["author", "title", "body", "public"]


class PostUpdateView(UpdateView):
    """Post Update View"""

    template_name = "posts/post_edit.html"
    model = Post
    fields = ["title", "body", "public"]
