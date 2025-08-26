from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class CatalogListView(ListView):
    model = Product
    # app_name/<model_name>_<action>


# def home(request):
#     product_list = Product.objects.all
#     context = {"products": product_list}
#     return render(request, "home.html", context)


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CatalogDetailView(DetailView):
    model = Product


# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk) #Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
