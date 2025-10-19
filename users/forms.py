from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class CustomUserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=35, help_text='Введите номер телефона')
    avatar = forms.ImageField(help_text='Загрузите аватар')
    country = forms.CharField(max_length=255, help_text='Введите страну проживания')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2', 'avatar', 'country', 'phone', )
