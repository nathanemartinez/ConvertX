from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    history = HistoricalRecords()

    @staticmethod
    def in_groups(groups, user):
        if user.groups.filter(name__in=groups).exists():
            return True
        return False

class Group(Group, models.Model):
    content = models.TextField(max_length=100, null=True, blank=True)

# Group.add_to_class('description', models.TextField(max_length=150, null=True, blank=False))

