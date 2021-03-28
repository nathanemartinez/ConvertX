from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from blog.models import Category
from blog.forms import CategoryModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin
User = get_user_model()


class CategoryListView(ListView):
	model = Category
	template_name = 'blog/models/category/list.html'
	paginate_by = PAG_BY
	queryset = Category.objects.display()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		context['obj'] = self.model
		return context


class CategoryDetailListView(DetailView, MultipleObjectMixin):
	model = Category
	template_name = 'blog/models/category/detail_list.html'
	paginate_by = PAG_BY

	def get_context_data(self, **kwargs):
		object_list = self.object.get_subcategories(4)
		context = super().get_context_data(object_list=object_list, **kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class CategoryCreateView(PermsRequiredMixin, CreateView):
	model = Category
	form_class = CategoryModelForm
	template_name = 'blog/models/category/create.html'
	perms = 'blog.add_category'
	extra_context = {
		'obj': Category,
		'images': True
	}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class CategoryUpdateView(PermsRequiredMixin, UpdateView):
	model = Category
	form_class = CategoryModelForm
	template_name = 'blog/models/category/update.html'
	perms = 'blog.change_category'
	extra_context = {
		'obj': Category,
		'images': True
	}

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class CategoryDeleteView(PermsRequiredMixin, DeleteView):
	model = Category
	template_name = 'blog/models/category/delete.html'
	perms = 'blog.delete_category'
	extra_context = {
		'obj': Category
	}

	def get_success_url(self):
		return self.model.get_list_url()
