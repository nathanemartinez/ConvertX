from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from users.forms import UserModelForm

User = get_user_model()


# class CategoryUpdateView(UpdateView):
# 	model = User
# 	form_class = UserModelForm
	# template_name =


def lockout(request):
	return render(request, 'users/general/lockout.html')

