from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from simple_history.models import HistoricalRecords
from users.managers import AssociationManager
from django.utils.translation import gettext as _


class User(AbstractUser):
    history = HistoricalRecords()

    @staticmethod
    def in_groups(groups, user):
        if user.groups.filter(name__in=groups).exists():
            return True
        return False


class Association(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('Permissions'),
        blank=True,
    )
    objects = AssociationManager()

    class Meta:
        verbose_name = _('Association')
        verbose_name_plural = _('Associations')

    def __str__(self):
        return self.name
