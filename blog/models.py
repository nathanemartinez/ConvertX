from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator


class TimeStampMixin(models.Model):
	date_created = models.DateTimeField(verbose_name=_("Date Created"), auto_now_add=True)
	date_updated = models.DateTimeField(verbose_name=_("Date Updated"), auto_now=True)

	class Meta:
		abstract = True


class NameMixin(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=500)

	class Meta:
		abstract = True


class ImageMixin(models.Model):
	alt_tag = models.CharField(verbose_name=_("Alt Tag"), max_length=50)
	caption = models.TextField(verbose_name=_("Caption"), max_length=100)

	class Meta:
		abstract = True


class AffiliateImage(ImageMixin):
	pass


class NormalImage(ImageMixin):
	pass


class Category(TimeStampMixin, NameMixin, ImageMixin):

	class Meta:
		ordering = ['name']
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	pass


class Tag(TimeStampMixin, NameMixin):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Tag"))

	def __str__(self):
		return self.name


class AffiliateProgram(TimeStampMixin, NameMixin):

	def __str__(self):
		return self.name


class TopMoneyPost(models.Model):
	affiliate_program = models.ManyToManyField(AffiliateProgram, verbose_name=_("Affiliate Program"))
	pass


class ReviewPost(models.Model):
	affiliate_program = models.ManyToManyField(AffiliateProgram, verbose_name=_("Affiliate Program"))
	pass


class InfoPost(models.Model):
	pass


class PostEstimates(models.Model):
	profit = models.IntegerField(verbose_name=_("Profit"))
	cost = models.IntegerField(verbose_name=_("Cost"))
	monthly_views = models.IntegerField(verbose_name=_("Monthly Views"))
	rank_difficulty = models.IntegerField(
		verbose_name=_("Rank Difficulty"),
		validators=[MaxValueValidator(5), MinValueValidator(1)]
	)


class Earnings(models.Model):
	pass


class Link(models.Model):
	# do follow, no follow
	follow = models.CharField(verbose_name=_("Follow"), max_length=10)
	link = models.URLField(verbose_name=_("Link"), max_length=500)


class AffiliateLink(models.Model):
	affiliate_tag = models.CharField(verbose_name=_("Affiliate Tag"), max_length=20)


class NormalLink(models.Model):
	pass


class ProductMixin(models.Model):
	sku_asin = models.CharField(verbose_name=_("Sku or Asin"), max_length=50)
	price = models.DecimalField(verbose_name=_("Price"), max_digits=9, decimal_places=2)
	currency = models.CharField(verbose_name=_("Currency"), default="USD", max_length=10)
	brand = models.CharField(verbose_name=_("Brand"), max_length=20)
	manufacturer = models.CharField(verbose_name=_("Manufacturer"), max_length=20)
	link = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name=_("Link"))
	affiliate_program = models.ForeignKey(AffiliateProgram, on_delete=models.CASCADE, verbose_name=_("Affiliate Program"))
	available = models.BooleanField(verbose_name=_("Available"), default=True)

	class Meta:
		abstract = True


class AffiliateProduct(ProductMixin):
	link = models.ForeignKey(AffiliateLink, on_delete=models.CASCADE, verbose_name=_("Link"))
	pass












