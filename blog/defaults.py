from django.contrib.auth import get_user_model
from .exceptions import DefaultUserError


def get_default_user():
	try:
		User = get_user_model()
		default_user = User.objects.filter(is_superuser=True, username='brickspy').first()
	except:
		raise DefaultUserError
	return default_user



