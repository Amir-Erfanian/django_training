from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("products/", views.product_list, name="product-list"),
    path("products/<int:id>/", views.product_detail, name="product-detail"),
    path("products/create/", views.product_create, name="product-create"),
    path("products/<int:id>/update/", views.product_update, name="product-update"),
    path("products/<int:id>/delete/", views.product_delete, name="product-delete"),
]
