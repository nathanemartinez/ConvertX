from django import forms
from blog.models import Category, SubCategory, AffiliateProgram, AffiliateTag
from django.forms.widgets import FileInput
from django.utils.translation import gettext as _

TIMESTAMP_EXCLUDE = ['creator', 'updater', 'created_at', 'updated_at']


class CategoryModelForm(forms.ModelForm):
	# file = forms.FileField(widget=FileInput)
	# file = forms.ImageField(label=_('File'), required=True, error_messages={'invalid': _("Image files only")}, widget=FileInput)
	# remove_photo = forms.BooleanField(required=False)

	class Meta:
		model = Category
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

