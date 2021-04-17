from .exceptions import MissingArgumentsError
from blog.exceptions import FileWarning
from django.conf import settings
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


# def extensions_checker(file_path):
# 	extension = magic.from_file(file_path, mime=True).split('/')[1].upper()
# 	if extension not in settings.MY_MEDIA_FILE_TYPES:
# 		os.remove(os.path.join(settings.MEDIA_ROOT, file_path))  # delete file
# 		raise FileWarning()


