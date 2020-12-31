from django.db import models


class StudentManager(models.Manager):
	def create_student(self, age):
		student = self.create(age=age)
		return student

	# def get_queryset(self):
	# 	return CustomQueryset
