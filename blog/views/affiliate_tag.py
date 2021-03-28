from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from blog.models import AffiliateProgram, AffiliateTag
from blog.forms import AffiliateTagModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
User = get_user_model()


class AffiliateTagListView(GroupsRequiredMixin, ListView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']
	extra_context = {
		'obj': AffiliateTag,
		'obj_affiliate_program': AffiliateProgram,
	}


class AffiliateTagDetailView(GroupsRequiredMixin, DetailView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/detail.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']


class AffiliateTagCreateView(PermsRequiredMixin, CreateView):
	model = AffiliateTag
	form_class = AffiliateTagModelForm
	template_name = 'blog/models/affiliate_tag/create.html'
	perms = 'blog.add_affiliatetag'
	extra_context = {
		'obj': AffiliateTag
	}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class AffiliateTagUpdateView(PermsRequiredMixin, UpdateView):
	model = AffiliateTag
	form_class = AffiliateTagModelForm
	template_name = 'blog/models/affiliate_tag/update.html'
	perms = 'blog.change_affiliatetag'
	extra_context = {
		'obj': AffiliateTag
	}

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class AffiliateTagDeleteView(PermsRequiredMixin, DeleteView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/delete.html'
	perms = 'blog.delete_affiliatetag'
	extra_context = {
		'obj': AffiliateTag
	}

	def get_success_url(self):
		return self.model.get_list_url()


