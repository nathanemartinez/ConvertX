from django.db import models


class AbstractQuerySet(models.QuerySet):
	def updated(self):
		return self.order_by('-updated_at')

	def display(self):
		return self.updated()


class CategoryQuerySet(AbstractQuerySet):
	pass


class SubCategoryQuerySet(AbstractQuerySet):
	pass


class AffiliateProgramQuerySet(AbstractQuerySet):
	pass


class TopMoneyPostQuerySet(models.QuerySet):
	def get_subcategory_posts(self, subcategory):
		return self.filter(subcategory=subcategory).order_by('-updated_at')
