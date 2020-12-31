# from django.db import models
#
#
# class ImageQuerySet(models.QuerySet):
#     def landscapes(self):
#         return self.filter(width__gte=models.F('height'))
#
#     def portraits(self):
#         return self.filter(width__lte=models.F('height'))
#
#     def small(self):
#         return self.filter(width__lte=1200)
#
#     def large(self):
#         return self.filter(width__gte=1200)