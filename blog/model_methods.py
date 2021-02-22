from django.shortcuts import reverse


class AbstractMethods:
	@staticmethod
	def get_create_str():
		return 'Create'

	@staticmethod
	def get_update_str():
		return 'Update'

	@staticmethod
	def get_delete_str():
		return 'Delete'


class CategoryMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:category-detail', kwargs={'pk': self.pk})

	def get_detail_list_url(self):
		return reverse('blog:category-detail-list', kwargs={'pk': self.pk})

	@staticmethod
	def get_list_url():
		return reverse('blog:category-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:category-create')

	# @staticmethod
	# def get_model_str():
	# 	return 'Category'


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

