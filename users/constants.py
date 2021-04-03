from convertx.constants import SUPERUSER_USERNAME
from django.core.exceptions import ObjectDoesNotExist
from users.exceptions import SuperuserDoesNotExist, SuperuserError, RequiredGroupsDoNotExist, RequiredGroupsError
import warnings


def get_user():
	from django.contrib.auth import get_user_model
	try:
		User = get_user_model()
		user = User.objects.get(is_superuser=True, username=SUPERUSER_USERNAME)
		return user
	except ObjectDoesNotExist:
		warnings.warn("Superuser does not exist")
		raise SuperuserDoesNotExist
	except:
		warnings.warn("Error getting superuser")
		raise SuperuserError


superuser = get_user()


def check_groups_exist(names: list):
	from users.models import Association
	if not names:
		warnings.warn("Required groups error")
		raise RequiredGroupsError
	for name in names:
		try:
			association = Association.objects.get(name=name)
		except ObjectDoesNotExist:
			warnings.warn("Required groups do not exist")
			raise RequiredGroupsDoNotExist
		except:
			warnings.warn("Required groups error")
			raise RequiredGroupsError
	return True


GROUPS = ['superuser', 'admin', 'blog admin']
check_groups_exist(GROUPS)
