from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ContactTemplateView, CatalogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>", CatalogDetailView.as_view(), name="product_detail"),
]
