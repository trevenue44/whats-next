from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views
from . import forms as custom_forms

urlpatterns = [
    path("register/", users_views.register, name="user-register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html",
            form_class=custom_forms.UserAuthenticationForm,
        ),
        name="user-login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="user-logout",
    ),
]
