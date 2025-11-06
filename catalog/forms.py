from django.forms import ModelForm
from django.core.exceptions import ValidationError


from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите название продукта",  # Текст подсказки внутри поля
            }
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Добавите изображение продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберете категорию продукта"}
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )



    def clean_price(self):

        price = self.cleaned_data.get("price")

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for forbidden_word in forbidden_words:
            if name == forbidden_word:
                self.add_error(
                    "name",
                    f"в названии присутствует запрещенное слово {forbidden_word}",
                )
            elif description == forbidden_word:
                self.add_error(
                    "description",
                    f"в описании присутствует запрещенное слово {forbidden_word}",
                )


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ('publish',)

    def __init__(self, *args, **kwargs):
        super(ProductModeratorForm, self).__init__(*args, **kwargs)

        self.fields["publish"].widget.attrs.update(
            {"class": "form-control"}
        )
