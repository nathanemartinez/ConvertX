from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import reverse, get_object_or_404, get_list_or_404
from blog.models import Category, SubCategory, TopMoneyPost
from blog.managers import CategoryManager
from blog.model_forms import CategoryModelForm
from blog.constants import PAG_BY


class CategoryListView(ListView):
	model = Category
	template_name = 'blog/models/category/category_list.html'
	paginate_by = PAG_BY

	def get_queryset(self):
		objs = Category.objects.display()
		return objs


class CategoryDetailListView(ListView):
	model = Category
	template_name = 'blog/models/category/category_detail.html'
	paginate_by = PAG_BY

	def get_queryset(self):
		obj = get_object_or_404(Category, pk=self.kwargs['pk'])
		objs = get_list_or_404(SubCategory, category=obj)
		return objs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
		return context


class CategoryCreateView(CreateView):
	model = Category
	form_class = CategoryModelForm
	permission_required = 'blog.add_category'
	template_name = 'blog/models/category/category_create.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class CategoryUpdateView(UpdateView):
	model = Category
	form_class = CategoryModelForm
	template_name = 'blog/models/category/category_update.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class CategoryDeleteView(DeleteView):
	model = Category
	template_name = 'blog/models/category/category_delete.html'
	context_object_name = 'category'

	def get_success_url(self):
		return reverse('home:home')


