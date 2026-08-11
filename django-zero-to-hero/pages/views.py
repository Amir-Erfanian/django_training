from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(
        request,
        "pages/home.html",
        {
            "name": "amir",
        },
    )


def about(request):
    return render(request, "pages/about.html", {"name": "amir"})


def product_list(request):
    products_list = Product.objects.all()
    return render(request, "pages/product_list.html", {"products": products_list})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "pages/product_detail.html", {"product": product})