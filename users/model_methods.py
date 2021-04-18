from django.shortcuts import reverse

class AbstractMethods:
	@staticmethod
	def get_view_str():
		return 'View'

	@staticmethod
	def get_list_str():
		return 'List'

	@staticmethod
	def get_create_str():
		return 'Create'

	@staticmethod
	def get_update_str():
		return 'Update'

	@staticmethod
	def get_delete_str():
		return 'Delete'

	@staticmethod
	def get_name_str():
		return 'Name'

	@staticmethod
	def get_description_str():
		return 'Description'

	@staticmethod
	def get_object_name():
		return 'Object'

	@staticmethod
	def get_object_strls():
		return 'Objects'


class UserMethods(AbstractMethods):
	def get_update_url(self):
		return reverse('users:user-update', kwargs={'pk': self.pk})

	@staticmethod
	def get_model_str():
		return 'User'

	@staticmethod
	def get_model_strl():
		return 'user'

	@staticmethod
	def get_model_strs():
		return 'Users'
