from tkinter.constants import CASCADE

from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория", related_name="products")
    price = models.IntegerField(verbose_name="цена")
    created_at = models.DateField(verbose_name="дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="дата последних изменений", auto_now_add=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "category", "created_at"]

    def __str__(self):
        return f"{self.name}, {self.price} , {self.category}"


