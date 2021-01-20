from django.shortcuts import render
from django.views.generic import TemplateView
from sentry_sdk import capture_message


class HomeView(TemplateView):
    template_name = 'home/home.html'


def error_400(request, exception=None):
    capture_message("400 error - custom page", level="error")
    return render(request, 'home/error_pages/400.html')


def error_403(request, exception=None):
    capture_message("403 error - custom page", level="error")
    return render(request, 'home/error_pages/403.html')


def error_404(request, exception=None):
    capture_message("404 error - custom page", level="error")
    return render(request, 'home/error_pages/404.html')


def error_500(request, exception=None):
    capture_message("500 error - custom page", level="error")
    return render(request, 'home/error_pages/500.html')

