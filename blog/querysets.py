from django.db import models



class CategoryQuerySet(models.QuerySet):
	def display(self):
		return self.order_by('-updated_at')


class SubCategoryQuerySet(models.QuerySet):
	def display(self):
		return self.order_by('-updated_at')


class TopMoneyPostQuerySet(models.QuerySet):
	def get_subcategory_posts(self, subcategory):
		return self.filter(subcategory=subcategory).order_by('-updated_at')



