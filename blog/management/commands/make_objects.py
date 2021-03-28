from django.core.management.base import BaseCommand
from blog.models import Category, AffiliateProgram
from blog.constants import user
from django.utils import timezone

class Command(BaseCommand):
	"""
	Make multiple objects.
	"""
	help = "Creates multiple objects"

	def add_arguments(self, parser):
		parser.add_argument("-c", "--category", type=int, help='')  # -d = command line, --deplay = in handle() method
		parser.add_argument("-p", "--program", type=int, help='')  # -d = command line, --deplay = in handle() method

	def handle(self, *args, **kwargs):
		if kwargs['category']:
			for i in range(kwargs['category']):
				now = timezone.now()
				options = {
					'name': f'Category {i}',
					'description': f'desc {i}',
					'creator': user,
					'updater': user,
					'created_at': now,
					'updated_at': now,
					'alt': 'hello',
					'caption': 'captionnn',
				}
				cat = Category.objects.create_category(**options)
			self.stdout.write("Created Categories.")

		elif kwargs['program']:
			for i in range(kwargs['program']):
				now = timezone.now()
				options = {
					'name': f'Affiliate Program {i} - New',
					'description': f'desc',
					'creator': user,
					'updater': user,
					'created_at': now,
					'updated_at': now,
				}
				program = AffiliateProgram.objects.create_affiliate_program(**options)
			self.stdout.write("Created Affiliate Programs.")
