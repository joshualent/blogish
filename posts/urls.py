from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/new", PostCreateView.as_view(), name="post_new"),
]
