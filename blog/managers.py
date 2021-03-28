from django.db import models
from .constants import MODEL_ARGS
from .utils import check_args
from blog.querysets import CategoryQuerySet


class AbstractManager(models.Manager):
	def delete_everything(self):
		self.all().delete()


class CategoryManager(AbstractManager):
	def create_category(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class SubCategoryManager(AbstractManager):
	def create_subcategory(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


# class TagManager(AbstractManager):
# 	def create_tag(self, **kwargs):
# 		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS']
# 		check_args(required_args, **kwargs)
# 		obj = self.create(**kwargs)
# 		return obj


class AffiliateProgramManager(AbstractManager):
	def create_affiliate_program(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyPostManager(AbstractManager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewPostManager(AbstractManager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoPostManager(AbstractManager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyProductManager(AbstractManager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewProductManager(AbstractManager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoProductManager(AbstractManager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class AffiliateTagManager(AbstractManager):
	def create_tag(self, **kwargs):
		required_args = MODEL_ARGS['REF_TAG_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyLinkManager(AbstractManager):
	def create_link(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['TOP_MONEY_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewLinkManager(AbstractManager):
	def create_link(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['REVIEW_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoLinkManager(AbstractManager):
	def create_link(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['INFO_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


# class NormalLinkManager(models.Manager):
# 	def create_product(self, **kwargs):
# 		required_args = MODEL_ARGS['LINK_ARGS']
# 		check_args(required_args, **kwargs)
# 		obj = self.create(**kwargs)
# 		return obj
