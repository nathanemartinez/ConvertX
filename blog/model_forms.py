from django import forms
from blog.models import Category
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
