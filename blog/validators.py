from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.conf import settings
from PIL import Image


def file_size(value):
	if value.size > settings.MY_MAX_FILE_SIZE:
		raise ValidationError(_("File too large. Size should not exceed 2MB."))


def invalid_characters(value):
	dots = value.path.count('.') > 1
	slashes = str(value).count('/') > 1
	if dots or slashes:
		raise ValidationError(_('Your file contains invalid characters (. , /)'))


def pil_verify_image(value):
	try:
		Image.open(value).verify()
	except:
		raise ValidationError(_('Invalid Image'))


# can't comment this out due to it being a dependency in migration file
def image_size(value):
	with Image.open(value) as img:
		if img.height < 300 or img.width < 700:
			raise ValidationError(_('Image too small. Must be at least 700x300.'))


# low this code doesn't work
def resize_image(value):
	try:
		with Image.open(value) as img:
			if img.height > 300 or img.width > 700:
				new_img = (300, 700)
				img.thumbnail(new_img)
				img.save(value)
	except:
		raise ValidationError("Image is invalid.")


