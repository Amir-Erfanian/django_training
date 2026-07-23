from django.urls import path
from mymodule import views

from django.contrib import admin

admin.site.site_header = "School Administration"
admin.site.site_title = "School Admin"
admin.site.index_title = "Welcome to the School Dashboard"

urlpatterns = [
    path('', views.index) ,
    path('about/', views.about),
    path('contact/', views.contact)
]