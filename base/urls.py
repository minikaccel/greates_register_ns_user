from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "base"


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="base:login"), name="logout"),
]