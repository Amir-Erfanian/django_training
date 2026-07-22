from django.urls import path

from myblog import views

utlpatterns = [
    path('', views.index, name='home-page'),
    path('posts', views.posts, name='posts-page'),
    path('post/<slug:slug>', views.post_detail, name='post-detail-page')
]