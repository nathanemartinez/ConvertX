from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from blog.models import SubCategory
from blog.forms import SubCategoryModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
User = get_user_model()


class SubCategoryListView(GroupsRequiredMixin, ListView):
	model = SubCategory
	template_name = 'blog/models/subcategory/list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']
	queryset = SubCategory.objects.display()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		context['obj'] = self.model
		return context


class SubCategoryDetailListView(DetailView, MultipleObjectMixin):
	model = SubCategory
	template_name = 'blog/models/subcategory/detail_list.html'
	paginate_by = PAG_BY

	def get_context_data(self, **kwargs):
		object_list = self.object.get_topmoneyposts(4)
		context = super().get_context_data(object_list=object_list, **kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class SubCategoryCreateView(PermsRequiredMixin, CreateView):
	model = SubCategory
	form_class = SubCategoryModelForm
	template_name = 'blog/models/subcategory/create.html'
	perms = 'blog.add_subcategory'
	extra_context = {
		'obj': SubCategory
	}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class SubCategoryUpdateView(PermsRequiredMixin, UpdateView):
	model = SubCategory
	form_class = SubCategoryModelForm
	template_name = 'blog/models/subcategory/update.html'
	perms = 'blog.change_subcategory'
	extra_context = {
		'obj': SubCategory
	}

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class SubCategoryDeleteView(PermsRequiredMixin, DeleteView):
	model = SubCategory
	template_name = 'blog/models/subcategory/delete.html'
	perms = 'blog.delete_subcategory'
	extra_context = {
		'obj': SubCategory
	}

	def get_success_url(self):
		return self.model.get_list_url()
