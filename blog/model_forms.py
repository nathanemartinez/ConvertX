from django import forms
from blog.models import Category
from django.forms.widgets import FileInput

TIMESTAMP_EXCLUDE = ['creator', 'updater', 'created_at', 'updated_at']


class CategoryModelForm(forms.ModelForm):
	file = forms.FileField(widget=FileInput)

	class Meta:
		model = Category
		exclude = TIMESTAMP_EXCLUDE
