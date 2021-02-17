from django.conf import settings
from .exceptions import DefaultUserError
from convertx.constants import SUPERUSER_USERNAME

try:
	User = settings.AUTH_USER_MODEL
	user = User.objects.get(pk=2)
	if (user.is_superuser is False) or (user.username != SUPERUSER_USERNAME):
		raise DefaultUserError
except:
	raise DefaultUserError


# low make this more DRY by using model fields
# Ex: https://stackoverflow.com/questions/38367226/django-get-all-required-fields
MODEL_ARGS = {
	'NAME_ARGS': ('name', 'description'),
	'TIMESTAMP_ARGS': ('creator', 'updater', 'created_at', 'updated_at'),
	'IMAGE_ARGS': ('alt_tag', 'caption'),
	'POST_ARGS': ('title', 'h1', 'meta', 'conclusion', 'category', 'tag', 'year', 'status'),
	'PRODUCT_ARGS': ('title', 'content', 'sku_asin', 'price', 'currency', 'affiliate_program', 'available'),
	'REF_TAG_ARGS': ('tag', 'program'),
	'LINK_ARGS': ('follow', 'link', 'anchor_text'),
	'TOP_MONEY_LINK': ('tag', 'product'),
	'REVIEW_LINK': ('tag', 'product'),
	'INFO_LINK': ('tag', 'product'),
}


