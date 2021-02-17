from django.core.management.base import BaseCommand
from blog.models import (Category, Tag, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct, TopMoneyLink,
						 PostMixin)


class Command(BaseCommand):
	help = 'Deletes the blog database.'

	def handle(self, *args, **kwargs):
		Category.objects.delete_everything()
		Tag.objects.delete_everything()
		AffiliateProgram.objects.delete_everything()
		AffiliateTag.objects.delete_everything()
		TopMoneyPost.objects.delete_everything()
		TopMoneyProduct.objects.delete_everything()
		TopMoneyLink.objects.delete_everything()
		PostMixin.objects.delete_everything()
		self.stdout.write('Task completed successfully')
