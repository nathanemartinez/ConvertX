from .exceptions import MissingArgumentsError
from PIL import Image
from uuid import uuid4
import os


def check_args(required, **kwargs):
	need = []
	for arg in required:
		if arg not in kwargs:
			need.append(arg)
	if (not need) == False:
		raise MissingArgumentsError(f"Missing required arguments: {need}")


def rename_path(instance, filename):
	upload_to = f'blog/images/{instance.creator.key}/'
	ext = filename.split('.')[-1]
	x = uuid4()
	filename = f'{str(x)[:13]}.{ext}'
	return os.path.join(upload_to, filename)


def resize_image(path):
	img = Image.open(path)

	if img.height > 300 or img.width > 700:
		new_img = (300, 700)
		img.thumbnail(new_img)
		img.save(path)
