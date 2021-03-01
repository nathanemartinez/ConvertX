from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import reverse, get_object_or_404, get_list_or_404
from blog.models import Category, SubCategory, TopMoneyPost
from blog.managers import CategoryManager
from blog.model_forms import CategoryModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from blog.mixins import GroupsRequiredMixin, PermsRequiredMixin
from blog.constants import ACCESS
User = get_user_model()


class CategoryListView(ListView):
	model = Category
	template_name = 'blog/models/category/category_list.html'
	paginate_by = PAG_BY

	def get_queryset(self):
		objs = Category.objects.display()
		return objs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		context['obj'] = Category
		return context


class CategoryDetailListView(ListView):
	model = Category
	template_name = 'blog/models/category/category_detail_list.html'
	paginate_by = PAG_BY

	def get_queryset(self):
		obj = get_object_or_404(Category, pk=self.kwargs['pk'])
		try:
			objs = SubCategory.objects.filter(category=obj)
		except ObjectDoesNotExist:
			return []
		return objs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = get_object_or_404(Category, pk=self.kwargs['pk'])
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class CategoryCreateView(PermsRequiredMixin, CreateView):
	model = Category
	form_class = CategoryModelForm
	template_name = 'blog/models/category/category_create.html'
	perms = 'blog.add_category'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class CategoryUpdateView(PermsRequiredMixin, UpdateView):
	model = Category
	form_class = CategoryModelForm
	template_name = 'blog/models/category/category_update.html'
	perms = 'blog.change_category'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class CategoryDeleteView(PermsRequiredMixin, DeleteView):
	model = Category
	template_name = 'blog/models/category/category_delete.html'
	perms = 'blog.delete_category'

	def get_success_url(self):
		return Category.get_list_url()


