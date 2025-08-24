from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all
    context = {"products": product_list}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) #Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)


