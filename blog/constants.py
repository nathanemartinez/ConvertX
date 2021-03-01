from django.contrib.auth import get_user_model
from .exceptions import DefaultUserError
from convertx.constants import SUPERUSER_USERNAME

try:
	User = get_user_model()
	user = User.objects.get(is_superuser=True, username=SUPERUSER_USERNAME)
except:
	raise DefaultUserError

# low make this more DRY by using model fields
# Ex: https://stackoverflow.com/questions/38367226/django-get-all-required-fields
MODEL_ARGS = {
	'NAME_ARGS': ('name', 'description'),
	'TIMESTAMP_ARGS': ('creator', 'updater', 'created_at', 'updated_at'),
	'IMAGE_ARGS': ('alt_tag', 'caption'),
	'POST_ARGS': ('title', 'h1', 'meta', 'conclusion', 'year', 'status'),
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

