# from django.core.management.base import BaseCommand
# from blog.models import Category, Tag, Site, Post, Product
#
#
# class Command(BaseCommand):
# 	help = 'Deletes the blog database.'
#
# 	def handle(self, *args, **kwargs):
# 		Category.objects.all().delete()
# 		Tag.objects.all().delete()
# 		Site.objects.all().delete()
# 		Post.objects.all().delete()
# 		Product.objects.all().delete()
# 		self.stdout.write('Task completed successfully')
