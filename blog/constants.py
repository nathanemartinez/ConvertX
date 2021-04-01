from django.contrib.auth import get_user_model
from convertx.constants import SUPERUSER_USERNAME
from django.conf import settings
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist
import warnings

# low make this more DRY by using model fields
# Ex: https://stackoverflow.com/questions/38367226/django-get-all-required-fields
MODEL_ARGS = {
	'NAME_ARGS': ('name', 'description'),
	'TIMESTAMP_ARGS': ('creator', 'updater', 'created_at', 'updated_at'),
	'IMAGE_ARGS': ('alt', 'caption'),
	'POST_ARGS': ('title', 'h1', 'meta', 'year', 'status'),
	'PRODUCT_ARGS': ('title', 'content', 'sku', 'price', 'currency', 'available'),
	'REF_TAG_ARGS': ('tag', 'program'),
	'LINK_ARGS': ('follow', 'link', 'anchor_text'),
	'TOP_MONEY_LINK': ('tag', 'product'),
	'REVIEW_LINK': ('tag', 'product'),
	'INFO_LINK': ('tag', 'product'),
}

ACCESS = {
	'MANAGE': ['superuser', 'admin', 'blog admin'],
	'CATEGORY': ['superuser', 'admin', 'blog admin']
}

PAG_BY = 10

# Caused an import error
# URLS = {
# 	'MANAGE': reverse('blog:manage')
# }