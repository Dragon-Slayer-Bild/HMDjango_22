from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.contrib.auth.models import Group


class CatalogListView(ListView):
    model = Product
    form_class = ProductForm


# app_name/<model_name>_<action>
# прошлая реализация
# def home(request):
#     product_list = Product.objects.all
#     context = {"products": product_list}
#     return render(request, "home.html", context)


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product


# прошлая реализация
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk) #Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user

        is_owner = (
                    self.object.owner == user)

        is_moderator = False

        try:
            moderator_group = Group.objects.get(name="Модератор продуктов")
            is_moderator = moderator_group in user.groups.all()
        except Group.DoesNotExist:
            pass
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при проверке группы модератора в get_form_class: {e}"))

        if is_owner:
            return ProductForm
        elif is_moderator:
            return ProductModeratorForm
        else:
            raise PermissionDenied("Непредвиденная ошибка доступа.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        is_owner = (
                self.request.user.is_authenticated and
                self.object.owner == self.request.user
        )

        is_moderator = False
        if self.request.user.is_authenticated:
            try:
                # Получаем группу "Модератор продуктов"
                moderator_group = Group.objects.get(name="Модератор продуктов")
                # Проверяем, есть ли пользователь в этой группе
                is_moderator = moderator_group in self.request.user.groups.all()
            except Group.DoesNotExist:
                pass
            except Exception as e:
                # Логирование ошибки, если что-то пошло не так
                self.stderr.write(self.style.ERROR(f"Ошибка при проверке группы модератора: {e}"))

        # Если пользователь не владелец и не модератор, запрещаем доступ
        if not (is_owner or is_moderator):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")

        return super().dispatch(request, *args, **kwargs)
