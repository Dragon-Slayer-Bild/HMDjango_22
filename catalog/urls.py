from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogListView,
    ContactTemplateView,
    CatalogDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, CatalogListViewByCategory,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>", cache_page(60)(CatalogDetailView.as_view()), name="product_detail"),
    path('product_list_by_category/<int:category_id>/', CatalogListViewByCategory.as_view(), name='product_list_by_category'),
]
