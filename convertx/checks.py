from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist
from convertx.constants import SUPERUSER_USERNAME
from convertx.exceptions import DefaultUserError
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