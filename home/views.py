from django.shortcuts import render
from django.views.generic import TemplateView
from sentry_sdk import capture_message
from blog.models import Category, TopMoneyPost

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tags = Tag.objects.all()
        categories = Category.objects.all()
        posts = TopMoneyPost.objects.all()
        categories = [categories[i:i + 3] for i in range(0, len(categories), 3)]
        # context['top_posts'] = Post.objects.top_10_posts()
        # context['tags1'] = tags[:len(tags)//2]
        # context['tags2'] = tags[len(tags)//2:]
        context['categories'] = categories
        context['posts'] = posts
        return context

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

