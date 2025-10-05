from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ContactTemplateView, CatalogDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>", CatalogDetailView.as_view(), name="product_detail"),
]
