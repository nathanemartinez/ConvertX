from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import reverse, get_object_or_404
from blog.models import Category
from blog.model_forms import CategoryModelForm


class CategoryListView(ListView):
	model = Category
	template_name = 'blog/models/category/category_list.html'


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'blog/models/category/category_detail.html'


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


