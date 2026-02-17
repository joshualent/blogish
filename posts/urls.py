from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostLikeView,
    CommentLikeView,
)


urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("posts/post/<int:post_pk>/like", PostLikeView.as_view(), name="post_like"),
    path(
        "posts/comment/<int:comment_pk>/like",
        CommentLikeView.as_view(),
        name="comment_like",
    ),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/new", PostCreateView.as_view(), name="post_new"),
]
