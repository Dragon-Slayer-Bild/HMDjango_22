from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="заголовок",
        help_text="Введите заголовок",
    )
    description = models.TextField(
        verbose_name="содержимое",
        help_text="содержимое блога",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="blog/preview",
        blank=True,
        null=True,
        verbose_name="превью",
        help_text="превью (изображение) блога",
    )
    created_at = models.DateField(verbose_name="дата создания", auto_now_add=True)
    publication = models.BooleanField(
        verbose_name="признак публикации",
        help_text="Проставьте признак публикации",
    )
    views = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="количество просмотров",
        help_text="количество просмотров",
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

    def __str__(self):
        return f"{self.title}"
