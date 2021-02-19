from django.db import models
from blog.constants import user


class CategoryQuerySet(models.QuerySet):
	def display(self):
		return self.order_by('-updated_at')

