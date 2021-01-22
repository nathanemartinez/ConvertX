from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce.models import HTMLField
from simple_history.models import HistoricalRecords

# todo change the default users to custom user like 'tester'


class TimeStampCreatorMixin(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_created_by', verbose_name=_("Created By"), null=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_updated_by', verbose_name=_("Updated By"), null=True)
	date_created = models.DateTimeField(verbose_name=_("Date Created"), auto_now_add=True)
	date_updated = models.DateTimeField(verbose_name=_("Date Updated"), auto_now=True)

	def __str__(self):
		return self.updated_by

	class Meta:
		abstract = True
		ordering = ['date_updated']
		verbose_name = _("Timestamp Creator Mixin")
		verbose_name_plural = _("Timestamp Creator Mixins")


class NameMixin(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=500)

	def __str__(self):
		return self.name

	class Meta:
		abstract = True
		ordering = ['name']
		verbose_name = _("Name Mixin")
		verbose_name_plural = _("Name Mixins")


class Category(NameMixin, TimeStampCreatorMixin):
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")


class Tag(NameMixin, TimeStampCreatorMixin):
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Tag")
		verbose_name_plural = _("Tags")


class AffiliateProgram(NameMixin, TimeStampCreatorMixin):
	history = HistoricalRecords()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Affiliate Program")
		verbose_name_plural = _("Affiliate Programs")


class PostEstimatesMixin(NameMixin, TimeStampCreatorMixin):
	monthly_profit = models.IntegerField(verbose_name=_("Profit"), validators=[MaxValueValidator(1000000), MinValueValidator(0)], null=True)
	cost = models.IntegerField(verbose_name=_("Cost"), validators=[MaxValueValidator(10000), MinValueValidator(0)], null=True)
	monthly_views = models.IntegerField(verbose_name=_("Monthly Views"), validators=[MaxValueValidator(1000000), MinValueValidator(0)], null=True)
	rank_difficulty = models.IntegerField(
		verbose_name=_("Rank Difficulty"),
		validators=[MaxValueValidator(5), MinValueValidator(1)]
	)

	def __str__(self):
		return self.name

	class Meta:
		abstract = True
		ordering = ['profit']
		verbose_name = _("Post Estimates")
		verbose_name_plural = _("Post Estimates")


class TopMoneyPostEstimates(PostEstimatesMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Top Money Post Estimates")
		verbose_name_plural = _("Top Money Post Estimates")


class ReviewPostEstimates(PostEstimatesMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Review Post Estimates")
		verbose_name_plural = _("Review Post Estimates")


class InfoPostEstimates(PostEstimatesMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Info Post Estimates")
		verbose_name_plural = _("Info Post Estimates")


class PostMixin(TimeStampCreatorMixin):
	DRAFT = 'D'
	HIDDEN = 'H'
	PUBLISHED = 'P'
	STATUS_CHOICES = (
		(DRAFT, 'Draft'),
		(HIDDEN, 'Hidden'),
		(PUBLISHED, 'Published'),
	)
	title = models.CharField(verbose_name=_("Title"), max_length=50)
	h1 = models.CharField(verbose_name=_("H1 Tag"), max_length=50)
	meta = models.CharField(verbose_name=_("Meta Tag"), max_length=250)
	conclusion = HTMLField(verbose_name=_("Conclusion"))
	# affiliate_program = models.ManyToManyField(AffiliateProgram, verbose_name=_("Affiliate Program"))
	category = models.ManyToManyField(Category, verbose_name=_("Category"))
	tag = models.ManyToManyField(Tag, verbose_name=_("Tag"))
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


class TopMoneyPost(PostMixin):
	post = models.OneToOneField(TopMoneyPostEstimates, on_delete=models.CASCADE, verbose_name=_("Top Money Post Estimates"), null=True)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Top Money Post")
		verbose_name_plural = _("Top Money Posts")


class ReviewPost(PostMixin):
	post = models.OneToOneField(ReviewPostEstimates, on_delete=models.CASCADE, verbose_name=_("Review Post Estimates"), null=True)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Review Post")
		verbose_name_plural = _("Review Posts")


class InfoPost(PostMixin):
	post = models.OneToOneField(InfoPostEstimates, on_delete=models.CASCADE, verbose_name=_("Info Post Estimates"), null=True)
	affiliate_program = None
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Info Post")
		verbose_name_plural = _("Info Posts")


class ProductMixin(TimeStampCreatorMixin):
	title = models.CharField(verbose_name=_("Title"), max_length=100)
	content = HTMLField()
	sku_asin = models.CharField(verbose_name=_("Sku or Asin"), max_length=50)
	price = models.DecimalField(verbose_name=_("Price"), max_digits=9, decimal_places=2)
	currency = models.CharField(verbose_name=_("Currency"), default="USD", max_length=10)
	brand = models.CharField(verbose_name=_("Brand"), max_length=20)
	manufacturer = models.CharField(verbose_name=_("Manufacturer"), max_length=20)
	affiliate_program = models.ManyToManyField(AffiliateProgram, verbose_name=_("Affiliate Program"))
	available = models.BooleanField(verbose_name=_("Available"), default=True)
	# todo add pros and cons, add keywords

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		ordering = ['title']
		verbose_name = _("Product Mixin")
		verbose_name_plural = _("Product Mixins")


class AffiliateProduct(ProductMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Affiliate Product")
		verbose_name_plural = _("Affiliate Products")


class ImageMixin(models.Model):
	alt_tag = models.CharField(verbose_name=_("Alt Tag"), max_length=50)
	caption = models.TextField(verbose_name=_("Caption"), max_length=100)

	def __str__(self):
		return self.alt_tag

	class Meta:
		abstract = True
		ordering = ['alt_tag']
		verbose_name = _("Image Mixin")
		verbose_name_plural = _("Image Mixins")


class AffiliateImage(ImageMixin):
	product = models.ForeignKey(AffiliateProduct, on_delete=models.CASCADE, verbose_name=_("Affiliate Product"), null=True)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Affiliate Image")
		verbose_name_plural = _("Affiliate Images")


class NormalImage(ImageMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Normal Image")
		verbose_name_plural = _("Normal Images")


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


class AffiliateTag(RefTagMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Affiliate Tag")
		verbose_name_plural = _("Affiliate Tags")


class LinkMixin(TimeStampCreatorMixin):
	# do follow, no follow
	# todo do follow/follow should be a charfield choice
	NO_FOLLOW = 'NF'
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


class AffiliateLink(LinkMixin):
	affiliate_tag = models.CharField(verbose_name=_("Affiliate Tag"), max_length=20)
	product = models.ForeignKey(AffiliateProduct, on_delete=models.CASCADE, verbose_name=_("Affiliate Product"), null=True)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Affiliate Link")
		verbose_name_plural = _("Affiliate Links")


class NormalLink(LinkMixin):
	history = HistoricalRecords()

	class Meta:
		verbose_name = _("Normal Link")
		verbose_name_plural = _("Normal Links")

