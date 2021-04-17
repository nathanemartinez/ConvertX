# from django.core.checks import Error, register, Tags
# from django.contrib.auth import get_user_model
# from convertx.constants import SUPERUSER_USERNAME
# from users.exceptions import SuperuserError, SuperuserDoesNotExist
# from django.core.exceptions import ObjectDoesNotExist
# import warnings
#
#
# def _check_super_user_exists():
# 	try:
# 		User = get_user_model()
# 		user = User.objects.get(is_superuser=True, username=SUPERUSER_USERNAME)
# 		return user
# 	except ObjectDoesNotExist:
# 		warnings.warn("Superuser does not exist")
# 		raise SuperuserDoesNotExist
# 	except:
# 		warnings.warn("Error getting superuser")
# 		raise SuperuserError
#
#
# @register(Tags.security, deploy=True)
# def check_super_user_exists(app_configs, **kwargs):
# 	errors = []
# 	if check_failed:
# 		errors.append(
# 			Error(
# 				'an error',
# 				hint='A hint.',
# 				obj=checked_object,
# 				id='myapp.E001',
# 			)
# 		)
# 	return errors