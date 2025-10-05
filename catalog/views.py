from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product




class CatalogListView(ListView):
    model = Product
    form_class = ProductForm

# app_name/<model_name>_<action>
#прошлая реализация
#def home(request):
#     product_list = Product.objects.all
#     context = {"products": product_list}
#     return render(request, "home.html", context)

class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CatalogDetailView(DetailView):
    model = Product

#прошлая реализация
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk) #Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url =  reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url =  reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url =  reverse_lazy('catalog:product_list')

