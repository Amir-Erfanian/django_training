from django.urls import path

from .views import home, about, contact, post_list, post_create, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('posts/', post_list, name='post_list'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/<int:id>/', post_detail, name='post_detail')
]
