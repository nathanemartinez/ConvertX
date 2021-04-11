from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.conf import settings
from PIL import Image


def file_size(value):
	if value.size > settings.MY_MAX_FILE_SIZE:
		raise ValidationError(_("File too large. Size should not exceed 2MB."))


def invalid_characters(value):
	if value.path.count('.') > 1:
		raise ValidationError(_('Multiple "." dots in file.'))


def pil_verify_image(value):
	try:
		Image.open(value).verify()
	except:
		raise ValidationError(_('Invalid Image'))
