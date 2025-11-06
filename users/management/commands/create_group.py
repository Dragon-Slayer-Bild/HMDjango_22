from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Создает группу и назначает права.'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            permission = Permission.objects.get(codename='can_unpublish_product')
            group.permissions.add(permission)
            permission = Permission.objects.get(codename='catalog.delete_product')
            group.permissions.add(permission)
        else:
            self.stdout.write(self.style.WARNING('Группа уже существует.'))