from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from convertx.constants import SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD


class Command(BaseCommand):
    help = 'Makes the site'

    @staticmethod
    def create_superuser():
        User = get_user_model()
        user = User.objects.create(username=SUPERUSER_USERNAME, email=SUPERUSER_EMAIL, password=SUPERUSER_PASSWORD)
        group = Group.objects.get(name='superuser')
        group.user_set.add(user)

    @staticmethod
    def create_groups():
        groups = Group.objects.bulk_create(
            Group(name='superuser'),
            Group(name='admin'),
            Group(name='blog admin'),
        )

    def handle(self, *args, **kwargs):
        self.create_groups()
        self.create_superuser()


