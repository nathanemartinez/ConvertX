from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    history = HistoricalRecords()


# Group.add_to_class()
# Group.add_to_class('description', models.CharField(max_length=180,null=True, blank=True))