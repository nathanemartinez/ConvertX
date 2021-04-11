from django import forms
from blog.models import Category, SubCategory, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct

TIMESTAMP_EXCLUDE = ['creator', 'updater', 'created_at', 'updated_at']
top_money_post_exclude = ['creator', 'updater', 'created_at', 'updated_at', 'slug']


class CategoryModelForm(forms.ModelForm):
	# file = forms.FileField(widget=FileInput)
	# file = forms.ImageField(label=_('File'), required=True, error_messages={'invalid': _("Image files only")}, widget=FileInput)
	# remove_photo = forms.BooleanField(required=False)
	
	class Meta:
		model = Category
		# high: security issue, do not use exclude
		exclude = TIMESTAMP_EXCLUDE


class SubCategoryModelForm(forms.ModelForm):
	class Meta:
		model = SubCategory
		exclude = TIMESTAMP_EXCLUDE


class AffiliateProgramModelForm(forms.ModelForm):
	class Meta:
		model = AffiliateProgram
		exclude = TIMESTAMP_EXCLUDE


class AffiliateTagModelForm(forms.ModelForm):
	class Meta:
		model = AffiliateTag
		fields = '__all__'


class TopMoneyPostModelForm(forms.ModelForm):

	class Meta:
		model = TopMoneyPost
		exclude = top_money_post_exclude


class TopMoneyProductModelForm(forms.ModelForm):
	class Meta:
		model = TopMoneyProduct
		exclude = TIMESTAMP_EXCLUDE
