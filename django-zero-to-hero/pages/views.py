from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


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


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("product-list")

    else:
        form = ProductForm()

    return render(request, "pages/product_form.html", {"form": form})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect("product-detail", id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "pages/product_update.html",
        {
            "form": form,
            "product": product,
        },
    )


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("product-list")

    return render(request, "pages/product_confirm_delete.html", {"product": product})
