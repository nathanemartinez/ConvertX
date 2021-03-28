from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from blog.models import AffiliateProgram
from blog.forms import AffiliateProgramModelForm
from blog.constants import PAG_BY, ACCESS
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin


class AffiliateProgramListView(GroupsRequiredMixin, ListView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']
	queryset = AffiliateProgram.objects.display()
	extra_context = {
		'obj': AffiliateProgram
	}


class AffiliateProgramDetailView(GroupsRequiredMixin, DetailView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/detail.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']


class AffiliateProgramCreateView(PermsRequiredMixin, CreateView):
	model = AffiliateProgram
	form_class = AffiliateProgramModelForm
	template_name = 'blog/models/affiliate_program/create.html'
	perms = 'blog.add_affiliateprogram'
	extra_context = {
		'obj': AffiliateProgram
	}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class AffiliateProgramUpdateView(PermsRequiredMixin, UpdateView):
	model = AffiliateProgram
	form_class = AffiliateProgramModelForm
	template_name = 'blog/models/affiliate_program/update.html'
	perms = 'blog.change_affiliateprogram'
	extra_context = {
		'obj': AffiliateProgram
	}

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class AffiliateProgramDeleteView(PermsRequiredMixin, DeleteView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/delete.html'
	perms = 'blog.delete_affiliateprogram'
	extra_context = {
		'obj': AffiliateProgram
	}

	def get_success_url(self):
		return self.model.get_list_url()
