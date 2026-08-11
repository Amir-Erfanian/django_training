from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("products/", views.product_list, name="product-list"),
    path("products/<int:id>/", views.product_detail, name="product-detail"),
]
