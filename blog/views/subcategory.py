from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from blog.models import SubCategory, TopMoneyPost
from blog.model_forms import CategoryModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
User = get_user_model()


class SubCategoryListView(GroupsRequiredMixin, ListView):
	model = SubCategory
	template_name = 'blog/models/subcategory/subcategory_list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']

	def get_queryset(self):
		objs = SubCategory.objects.display()
		return objs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		context['obj'] = SubCategory
		return context


class SubCategoryDetailListView(ListView):
	model = SubCategory
	template_name = 'blog/models/subcategory/subcategory_detail_list.html'
	paginate_by = PAG_BY

	def get_queryset(self):
		obj = get_object_or_404(SubCategory, pk=self.kwargs['pk'])
		try:
			objs = TopMoneyPost.objects.get_subcategory_posts(subcategory=obj)
		except ObjectDoesNotExist:
			return []
		return objs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = get_object_or_404(SubCategory, pk=self.kwargs['pk'])
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class SubCategoryCreateView(PermsRequiredMixin, CreateView):
	model = SubCategory
	form_class = CategoryModelForm
	template_name = 'blog/models/subcategory/subcategory_create.html'
	perms = 'blog.add_category'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class SubCategoryUpdateView(PermsRequiredMixin, UpdateView):
	model = SubCategory
	form_class = CategoryModelForm
	template_name = 'blog/models/subcategory/subcategory_update.html'
	perms = 'blog.change_category'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class SubCategoryDeleteView(PermsRequiredMixin, DeleteView):
	model = SubCategory
	template_name = 'blog/models/subcategory/subcategory_delete.html'
	perms = 'blog.delete_category'

	def get_success_url(self):
		return SubCategory.get_list_url()


