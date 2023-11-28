from django.urls import path
from . import views
from professor import views
from .views import SignUpView, SignInView, signout

app_name = "professor"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
]