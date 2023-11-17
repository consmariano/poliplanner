from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/<int:pk>/', views.post_single, name="post_single"),
]
