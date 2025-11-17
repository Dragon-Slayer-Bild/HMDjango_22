from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHES_ENABLED

def get_product_list_fom_cache():
    """Получает данные по продуктам из кэша,если кэш пуст, получает данные из БД"""
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products

class ProductService:

    @staticmethod
    def get_products_by_category(category):
        try:
            products = Product.objects.filter(category=category, available=True)
            return list(products)
        except Category.DoesNotExist:
            return []

    @staticmethod
    def get_all_categories():
        """
        Возвращает список всех категорий.
        """
        return list(Category.objects.all())