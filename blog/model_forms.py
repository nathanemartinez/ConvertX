from django import forms
from blog.models import Category

TIMESTAMP_EXCLUDE = ('creator', 'updater', 'created_at', 'updated_at')


class CategoryModelForm(forms.ModelForm):
	class Meta:
		model = Category
		exclude = TIMESTAMP_EXCLUDE
