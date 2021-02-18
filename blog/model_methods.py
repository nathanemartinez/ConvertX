from django.shortcuts import reverse


class CategoryMethods:
	@staticmethod
	def get_list_url():
		return reverse('blog:category-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:category-create')

	@staticmethod
	def get_model_str():
		return 'Category'


class TagMethods:
	@staticmethod
	def get_model_str():
		return 'Tag'


class AffiliateProgramMethods:
	@staticmethod
	def get_model_str():
		return 'Affiliate Program'


class AffiliateTagMethods:
	@staticmethod
	def get_model_str():
		return 'Affiliate Tag'


class TopMoneyPostMethods:
	@staticmethod
	def get_model_str():
		return 'Top Money Post'


class TopMoneyProductMethods:
	@staticmethod
	def get_model_str():
		return 'Top Money Product'

