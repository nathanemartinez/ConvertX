from django.db import models
from .constants import MODEL_ARGS
from .utils import check_args


class CategoryManager(models.Manager):
	def create_category(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TagManager(models.Manager):
	def create_tag(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class AffiliateProgramManager(models.Manager):
	def create_affiliate_program(self, **kwargs):
		required_args = MODEL_ARGS['NAME_ARGS'] + MODEL_ARGS['TIMESTAMP_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyPostManager(models.Manager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewPostManager(models.Manager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoPostManager(models.Manager):
	def create_post(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['POST_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyProductManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewProductManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoProductManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['TIMESTAMP_ARGS'] + MODEL_ARGS['IMAGE_ARGS'] + MODEL_ARGS['PRODUCT_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class AffiliateTagManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['REF_TAG_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class TopMoneyLinkManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['TOP_MONEY_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class ReviewLinkManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['REVIEW_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class InfoLinkManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS'] + MODEL_ARGS['INFO_LINK']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj


class NormalLinkManager(models.Manager):
	def create_product(self, **kwargs):
		required_args = MODEL_ARGS['LINK_ARGS']
		check_args(required_args, **kwargs)
		obj = self.create(**kwargs)
		return obj
