from django.urls import path

from .views import (
    home,
    about,
    contact,
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    register,
    profile,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("posts/", post_list, name="post_list"),
    path("posts/create/", post_create, name="post_create"),
    path("posts/<int:id>/", post_detail, name="post_detail"),
    path("posts/<int:id>/edit/", post_update, name="post_update"),
    path("posts/<int:id>/delete/", post_delete, name="post_delete"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "register/",
        register,
        name="register",
    ),
    path(
    'profile/',
    profile,
    name='profile',
),
]
