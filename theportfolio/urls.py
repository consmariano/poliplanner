from django.urls import path
from . import views
from .views import (
    home,
    post_list,
    single_post,
    create_post,
    edit_post,
    remove_post,
)
#from .views import HomeView, PostsListView, SinglePostDetailView, EditPostView, CreatePostView, RemovePostView

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', single_post, name='post_single'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/edit/<int:pk>/', edit_post, name='edit_post'),
    path('posts/remove/<int:pk>/', remove_post, name='remove_post'),
]

# urlpatterns = [
#     path('', HomeView.as_view(), name="home"),
#     path('posts/', PostsListView.as_view(), name="post_list"),
#     path('posts/<int:pk>/', SinglePostDetailView.as_view(), name="post_single"),
#     path('create_post/', CreatePostView.as_view(), name="create_post"),
#     path('posts/editar/<int:pk>', EditPostView.as_view(), name="edit_post"),
#     path('posts/<int:pk>/remover', RemovePostView.as_view(), name="remove_post"),
# ]
