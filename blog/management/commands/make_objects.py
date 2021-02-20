from django.core.management.base import BaseCommand
from blog.models import Category
from blog.constants import user
from django.utils import timezone

class Command(BaseCommand):
	"""
	Make multiple objects.
	"""
	help = "Creates multiple objects"

	def add_arguments(self, parser):
		parser.add_argument("-c", "--category", type=int, help='')  # -d = command line, --deplay = in handle() method

	def handle(self, *args, **kwargs):
		if kwargs['category']:
			for i in range(1, 11):
				now = timezone.now()
				options = {
					'name': f'Category {i}',
					'description': f'desc {i}',
					'creator': user,
					'updater': user,
					'created_at': now,
					'updated_at': now,
					'alt_tag': 'hello',
					'caption': 'captionnn',
				}
				cat = Category.objects.create_category(**options)
			self.stdout.write("Created Categories.")
