from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CustomUserRegisterForm
from config.settings import EMAIL_HOST_USER
import secrets

from .models import User


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('catalog: product_list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
                subject = 'Подтверждение почты',
                message = f'Приветствуем, перейдите по ссылке для подтверждения  {url}',
                from_email = EMAIL_HOST_USER,
                recipient_list = [user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
