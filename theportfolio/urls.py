from django.urls import path
from . import views
from .views import HomeView, PostsListView, SinglePostDetailView, EditPostView, CreatePostView, RemovePostView, AddCommentView, AddCategoryView, CategoryView, ListCategoriesView
from .views import login, cadastro

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('', HomeView.as_view(), name="home"),
    path('posts/', PostsListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', SinglePostDetailView.as_view(), name="post_single"),
    path('create_post/', CreatePostView.as_view(), name="create_post"),
    path('create_category/', AddCategoryView.as_view(), name="create_category"),
    path('posts/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('posts/<int:pk>/remove', RemovePostView.as_view(), name="remove_post"),
    path('posts/<int:pk>/coment', AddCommentView.as_view(), name="create_comment"),
    path('category/<int:cats>/', CategoryView, name="categories"),
    path('categories/', ListCategoriesView.as_view(), name="list_categories"),
]

