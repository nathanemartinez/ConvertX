from django.shortcuts import render, reverse
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from users.forms import UserModelForm
from django.contrib.auth.mixins import UserPassesTestMixin

User = get_user_model()


class UserUpdateView(UserPassesTestMixin, UpdateView):
	model = User
	form_class = UserModelForm
	template_name = 'users/user/update.html'

	def get_success_url(self):
		return reverse('home:home')

	def test_func(self):
		is_superuser = self.request.user.is_superuser
		is_user = self.request.user == self.get_object()
		return is_superuser and is_user


def lockout(request):
	return render(request, 'users/general/lockout.html')

