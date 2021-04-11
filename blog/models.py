from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce.models import HTMLField
from simple_history.models import HistoricalRecords
from blog.validators import file_size, invalid_characters, pil_verify_image
from blog.managers import (CategoryManager, SubCategoryManager, AffiliateProgramManager, TopMoneyPostManager, ReviewPostManager,
						   InfoPostManager, TopMoneyProductManager, ReviewProductManager, InfoProductManager,
						   AffiliateTagManager, TopMoneyLinkManager, ReviewLinkManager, InfoLinkManager,
						   )
from blog.utils import rename_path, resize_image
from blog.model_methods import (CategoryMethods, SubCategoryMethods, AffiliateProgramMethods, AffiliateTagMethods, \
								PostMixinMethods, TopMoneyPostMethods, TopMoneyProductMethods)
from blog.querysets import CategoryQuerySet, SubCategoryQuerySet, AffiliateProgramQuerySet, TopMoneyPostQuerySet
# low change the default users to custom user like 'tester'
# low add "display" field to all models. like category model


class TimeStampCreatorMixin(models.Model):
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_creator', verbose_name=_("Creator"), null=True)
	updater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_updater', verbose_name=_("Updater"), null=True)
	created_at = models.DateTimeField(verbose_name=_("Date Created"), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_("Date Updated"), auto_now=True)

	def __str__(self):
		return self.updater

	class Meta:
		abstract = True
		ordering = ['updated_at']
		verbose_name = _("Timestamp Creator Mixin")
		verbose_name_plural = _("Timestamp Creator Mixins")


class NameMixin(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		abstract = True
		ordering = ['name']
		verbose_name = _("Name Mixin")
		verbose_name_plural = _("Name Mixins")


class ImageMixin(models.Model):
	alt = models.CharField(verbose_name=_("Alt Tag"), max_length=50, null=True)
	caption = models.CharField(verbose_name=_("Caption"), max_length=100, null=True)
	file = models.ImageField(verbose_name=_("File"), upload_to=rename_path, max_length=70,
							 validators=[file_size, invalid_characters, pil_verify_image])

	def __str__(self):
		return self.alt

	def save(self, *args, **kwargs):
		super(ImageMixin, self).save()
		if self.file:
			resize_image(self.file.path)

	class Meta:
		abstract = True
		ordering = ['alt']
		verbose_name = _("Image Mixin")
		verbose_name_plural = _("Image Mixins")


class Category(NameMixin, TimeStampCreatorMixin, ImageMixin, CategoryMethods):
	objects = CategoryManager.from_queryset(CategoryQuerySet)()
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

	def get_subcategories(self, number=None):
		if number:
			return self.subcategory_set.all()[:number]
		return self.subcategory_set.all()


class SubCategory(NameMixin, TimeStampCreatorMixin, SubCategoryMethods):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"), null=True)
	objects = SubCategoryManager.from_queryset(SubCategoryQuerySet)()
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Sub Category")
		verbose_name_plural = _("Sub Categories")

	def get_topmoneyposts(self, number=None):
		if number:
			return self.topmoneypost_set.all()[:number]
		return self.topmoneypost_set.all()


class PostMixin(TimeStampCreatorMixin, ImageMixin, PostMixinMethods):
	DRAFT = 'D'
	HIDDEN = 'H'
	PUBLISHED = 'P'
	STATUS_CHOICES = (
		(DRAFT, 'Draft'),
		(HIDDEN, 'Hidden'),
		(PUBLISHED, 'Published'),
	)
	title = models.CharField(verbose_name=_("Title"), max_length=50)
	slug = models.SlugField(blank=True)
	h1 = models.CharField(verbose_name=_("H1 Tag"), max_length=50)
	meta = models.CharField(verbose_name=_("Meta Tag"), max_length=250)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_("Sub Category"), null=True)
	# tag = models.ManyToManyField(Tag, verbose_name=_("Tag"))
	year = models.IntegerField(
		verbose_name=_("Year"),
		validators=[MaxValueValidator(3000), MinValueValidator(2020)],
		blank=True,
		null=True
	)
	status = models.CharField(verbose_name="Status", max_length=1, choices=STATUS_CHOICES)
	# todo add keywords

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		ordering = ['title']
		verbose_name = _("Post Mixin")
		verbose_name_plural = _("Post Mixins")

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug.
			self.slug = slugify(self.title)

		super().save(*args, **kwargs)


class AffiliateProgram(NameMixin, TimeStampCreatorMixin, AffiliateProgramMethods):
	objects = AffiliateProgramManager.from_queryset(AffiliateProgramQuerySet)()
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Affiliate Program")
		verbose_name_plural = _("Affiliate Programs")


class TopMoneyPost(PostMixin, TopMoneyPostMethods):
	# low make sure there are no h1, h2, etc tags in these
	intro = HTMLField(verbose_name=_("Intro"), null=True)
	outro = HTMLField(verbose_name=_("Outro"), null=True)
	objects = TopMoneyPostManager.from_queryset(TopMoneyPostQuerySet)()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Top Money Post")
		verbose_name_plural = _("Top Money Posts")

	def get_topmoneyproducts(self, number=None):
		if number:
			return self.topmoneyproduct_set.all()[:number]
		return self.topmoneyproduct_set.all()


class ReviewPost(PostMixin):
	objects = ReviewPostManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Review Post")
		verbose_name_plural = _("Review Posts")


class InfoPost(PostMixin):
	affiliate_program = None
	objects = InfoPostManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Info Post")
		verbose_name_plural = _("Info Posts")


class ProductMixin(TimeStampCreatorMixin, ImageMixin):
	title = models.CharField(verbose_name=_("Title"), max_length=100)
	content = HTMLField()
	sku = models.CharField(verbose_name=_("Sku or Asin"), max_length=50)
	price = models.DecimalField(verbose_name=_("Price"), max_digits=9, decimal_places=2)
	currency = models.CharField(verbose_name=_("Currency"), default="USD", max_length=10)
	available = models.BooleanField(verbose_name=_("Available"), default=True)

	# todo add pros and cons, add keywords

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		ordering = ['title']
		verbose_name = _("Product Mixin")
		verbose_name_plural = _("Product Mixins")


class TopMoneyProduct(ProductMixin, TopMoneyProductMethods):
	post = models.ForeignKey(TopMoneyPost, on_delete=models.CASCADE, verbose_name=_("Post"), null=True)
	objects = TopMoneyProductManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Top Money Product")
		verbose_name_plural = _("Top Money Products")

	def get_link(self):
		return self.topmoneylink.link


class ReviewProduct(ProductMixin):
	post = models.ForeignKey(ReviewPost, on_delete=models.CASCADE, verbose_name=_("Post"), null=True)
	objects = ReviewProductManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Review Product")
		verbose_name_plural = _("Review Products")


class InfoProduct(ProductMixin):
	post = models.ForeignKey(InfoPost, on_delete=models.CASCADE, verbose_name=_("Post"), null=True)
	objects = InfoProductManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Info Product")
		verbose_name_plural = _("Info Products")


class RefTagMixin(models.Model):
	tag = models.CharField(verbose_name=_("Tag"), max_length=20)
	program = models.ForeignKey(AffiliateProgram, on_delete=models.CASCADE, verbose_name=_("Affiliate Program"), null=True)

	def __str__(self):
		return self.tag

	class Meta:
		abstract = True
		ordering = ['tag']
		verbose_name = _("Ref Mixin")
		verbose_name_plural = _("Ref Mixins")


class AffiliateTag(RefTagMixin, AffiliateTagMethods):
	objects = AffiliateTagManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Affiliate Tag")
		verbose_name_plural = _("Affiliate Tags")


class LinkMixin(TimeStampCreatorMixin):
	# do follow, no follow
	# todo do follow/follow should be a charfield choice
	NO_FOLLOW = 'NF'
	NO_FOLLOW_TEXT = 'nofollow'
	DO_FOLLOW = 'DF'
	STATUS_CHOICES = (
		(NO_FOLLOW, 'No Follow'),
		(DO_FOLLOW, 'Do Follow'),
	)
	follow = models.CharField(verbose_name=_("Follow"), max_length=10, choices=STATUS_CHOICES)
	link = models.URLField(verbose_name=_("Link"), max_length=500)
	anchor_text = models.CharField(verbose_name=_("Anchor Text"), max_length=30)

	def __str__(self):
		return self.anchor_text

	class Meta:
		abstract = True
		ordering = ['anchor_text']
		verbose_name = _("Link Mixin")
		verbose_name_plural = _("Link Mixins")

	def get_follow_choice(self):
		if self.follow == self.NO_FOLLOW:
			return False
		return True


class TopMoneyLink(LinkMixin):
	tag = models.ForeignKey(AffiliateTag, on_delete=models.CASCADE, verbose_name=_("Affiliate Tag"), null=True)
	product = models.OneToOneField(TopMoneyProduct, on_delete=models.CASCADE, verbose_name=_("Product"), null=True)
	objects = TopMoneyLinkManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Top Money Link")
		verbose_name_plural = _("Top Money Links")


class ReviewLink(LinkMixin):
	tag = models.ForeignKey(AffiliateTag, on_delete=models.CASCADE, verbose_name=_("Affiliate Tag"), null=True)
	product = models.ForeignKey(ReviewProduct, on_delete=models.CASCADE, verbose_name=_("Product"), null=True)
	objects = ReviewLinkManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Review Link")
		verbose_name_plural = _("Review Links")


class InfoLink(LinkMixin):
	tag = models.ForeignKey(AffiliateTag, on_delete=models.CASCADE, verbose_name=_("Affiliate Tag"), null=True)
	product = models.ForeignKey(InfoProduct, on_delete=models.CASCADE, verbose_name=_("Product"), null=True)
	objects = InfoLinkManager()
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Info Link")
		verbose_name_plural = _("Info Links")
