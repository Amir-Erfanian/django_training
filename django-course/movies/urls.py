from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:id>/', views.movie_detail, name='movie_detail'),
]