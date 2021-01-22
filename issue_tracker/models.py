from django.db import models
from blog.models import NameMixin, TimeStampCreatorMixin


class Tracker(NameMixin, TimeStampCreatorMixin):
	pass


class Project(NameMixin, TimeStampCreatorMixin):
	pass

# todo add a comment functionaltity
class Issue(NameMixin, TimeStampCreatorMixin):
	"""
	issue type, issue status,
	"""
	pass
