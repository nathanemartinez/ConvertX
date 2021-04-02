from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist
from convertx.constants import SUPERUSER_USERNAME, GROUPS
from convertx.exceptions import DefaultUserError, RequiredGroupDoNotExist
from users.models import Association
import warnings


try:
	User = get_user_model()
	user = User.objects.get(is_superuser=True, username=SUPERUSER_USERNAME)
except OperationalError:
	pass
except ObjectDoesNotExist:
	warnings.warn("Superuser does not exist")
except:
	raise DefaultUserError


def check_groups_exist(names: list):
	for name in names:
		association = Association.objects.get(name=name)
		if not association.exists():
			raise RequiredGroupDoNotExist


check_groups_exist(GROUPS)


