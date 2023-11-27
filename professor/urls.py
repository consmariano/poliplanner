from django.urls import path
from . import views
from professor import views

app_name = "professor"

urlpatterns = [
    #path('register/', UserRegisterView.as_view(), name = 'register'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
]