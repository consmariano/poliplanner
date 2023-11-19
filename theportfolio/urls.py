from django.urls import path
from . import views
from .views import HomeView, PostsListView, SinglePostDetailView, EditPostView, CreatePostView, RemovePostView, AddCommentView, CreateCategoryView, SingleCatsDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('posts/', PostsListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', SinglePostDetailView.as_view(), name="post_single"),
    path('categorias/<str:cats>/', SingleCatsDetailView.as_view(), name="category_single"),
    path('create_post/', CreatePostView.as_view(), name="create_post"),
    path('categorias/', CreateCategoryView.as_view(), name="create_category"),
    path('posts/editar/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('posts/<int:pk>/remover', RemovePostView.as_view(), name="remove_post"),
    path('posts/<int:pk>/comentario', AddCommentView.as_view(), name="create_comment"),
]

