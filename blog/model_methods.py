from django.shortcuts import reverse
from blog import models
from blog.exceptions import MissingChoiceError


class AbstractMethods:
	@staticmethod
	def get_view_str():
		return 'View'

	@staticmethod
	def get_list_str():
		return 'List'

	@staticmethod
	def get_create_str():
		return 'Create'

	@staticmethod
	def get_update_str():
		return 'Update'

	@staticmethod
	def get_delete_str():
		return 'Delete'

	@staticmethod
	def get_name_str():
		return 'Name'

	@staticmethod
	def get_description_str():
		return 'Description'

	@staticmethod
	def get_object_name():
		return 'Object'

	@staticmethod
	def get_object_strls():
		return 'Objects'


class PostMixinMethods:
	@staticmethod
	def get_choice_display(choice):
		if choice == models.PostMixin.DRAFT:
			return 'draft'
		elif choice == models.PostMixin.HIDDEN:
			return 'hidden'
		elif choice == models.PostMixin.PUBLISHED:
			return 'published'
		else:
			raise MissingChoiceError()


class CategoryMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:category-detail-list', kwargs={'pk': self.pk})

	def get_detail_list_url(self):
		return reverse('blog:category-detail-list', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:category-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:category-delete', kwargs={'pk': self.pk})

	@staticmethod
	def get_list_url():
		return reverse('blog:category-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:category-create')

	@staticmethod
	def get_model_str():
		return 'Category'

	@staticmethod
	def get_model_strl():
		return 'category'

	@staticmethod
	def get_model_strs():
		return 'Categories'


class SubCategoryMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:subcategory-detail-list', kwargs={'pk': self.pk})

	def get_detail_list_url(self):
		return reverse('blog:subcategory-detail-list', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:subcategory-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:subcategory-delete', kwargs={'pk': self.pk})

	@staticmethod
	def get_list_url():
		return reverse('blog:subcategory-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:subcategory-create')

	@staticmethod
	def get_model_str():
		return 'Subcategory'

	@staticmethod
	def get_model_strl():
		return 'subcategory'

	@staticmethod
	def get_model_strs():
		return 'Subcategories'


class AffiliateProgramMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:affiliate-program-detail', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:affiliate-program-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:affiliate-program-delete', kwargs={'pk': self.pk})

	@staticmethod
	def get_list_url():
		return reverse('blog:affiliate-program-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:affiliate-program-create')

	@staticmethod
	def get_model_str():
		return 'Affiliate Program'

	@staticmethod
	def get_model_strl():
		return 'affiliate program'

	@staticmethod
	def get_model_strs():
		return 'Affiliate Programs'


class AffiliateTagMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:affiliate-tag-detail', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:affiliate-tag-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:affiliate-tag-delete', kwargs={'pk': self.pk})

	@staticmethod
	def get_list_url():
		return reverse('blog:affiliate-tag-list')

	@staticmethod
	def get_create_url():
		return reverse('blog:affiliate-tag-create')

	@staticmethod
	def get_model_str():
		return 'Affiliate Tag'

	@staticmethod
	def get_model_strl():
		return 'affiliate tag'

	@staticmethod
	def get_model_strs():
		return 'Affiliate Tags'

	@staticmethod
	def get_name_str():
		return 'Tag'


class TopMoneyPostMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:top-money-post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

	def get_update_url(self):
		return reverse('blog:top-money-post-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:top-money-post-delete', kwargs={'pk': self.pk})

	# Used in manage
	def get_list_url(self):
		return reverse('blog:manage')

	def get_list_detail_url(self):
		return reverse('blog:top-money-post-list-detail', kwargs={'pk': self.pk})

	@staticmethod
	def get_create_url():
		return reverse('blog:top-money-post-create')

	@staticmethod
	def get_model_str():
		return 'Top money post'

	@staticmethod
	def get_model_strl():
		return 'top money post'

	@staticmethod
	def get_model_strs():
		return 'Top money posts'


class TopMoneyProductMethods(AbstractMethods):
	def get_absolute_url(self):
		return reverse('blog:top-money-product-detail', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:top-money-product-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:top-money-product-delete', kwargs={'pk': self.pk})

	def get_post_url(self):
		return reverse('blog:top-money-post-list-detail', kwargs={'pk': self.post.pk})

	@staticmethod
	def get_create_url():
		return reverse('blog:top-money-product-create')

	@staticmethod
	def get_model_str():
		return 'Top money product'

	@staticmethod
	def get_model_strl():
		return 'top money product'

	@staticmethod
	def get_model_strs():
		return 'Top money products'

	@staticmethod
	def get_post_str():
		return 'Post'

