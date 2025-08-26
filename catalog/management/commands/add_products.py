from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test product to the database"

    def handle(self, *args, **kwargs):

        product_to_delete = Product.objects.all()
        product_to_delete.delete()
        category_to_delete = Category.objects.all()
        category_to_delete.delete()

        category, created = Category.objects.get_or_create(
            name="Электроника", description="части и компоненты"
        )

        products = [
            {"name": "Провод", "description": "провода двужильный", "price": 555},
            {"name": "Схема", "description": "Схема для пайки", "price": 222},
            {"name": "Чип", "description": "контрольный чип", "price": 999},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(
            name = product['name'],
            description = product['description'],
            price = product['price'],
            category = category)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))