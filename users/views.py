from django.shortcuts import render


def lockout(request):
	return render(request, 'users/general/lockout.html')
