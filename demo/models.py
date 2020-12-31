# from django.db import models
# from .managers import StudentManager
# from django.urls import reverse
#
#
# class Common(models.Model):
# 	name = models.CharField(max_length=100)
#
# 	def __str__(self):
# 		return self.name
#
# 	def get_absolute_url(self):
# 		return reverse('people.views.details', args=[str(self.id)])
#
# 	class Meta:
# 		abstract = True
#
#
# class Student(Common):
# 	age = models.IntegerField()
# 	objects = StudentManager()
#
	# @classmethod
	# def create(cls, age):
	# 	student = cls(age=age)
	# 	return student
	#
	# @staticmethod
	# 	def get_create_url():
	# 	return reverse('bug_tracker:main-profile-create')

# 	class Meta(Common.Meta):
# 		ordering = ['age']
#
#
# class Person(models.Model):
# 	SHIRT_SIZES = (
# 		('S', 'Small'),
# 		('M', 'Medium'),
# 		('L', 'Large'),
# 	)
# 	name = models.CharField(max_length=60)
# 	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
# 	date_created = models.DateField()
#
# 	class Meta:
# 		ordering = ['date_created']
# 		verbose_name_plural = 'People'
