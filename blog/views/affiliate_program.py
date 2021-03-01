from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from blog.models import AffiliateProgram
from blog.model_forms import AffiliateProgramModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
User = get_user_model()


class AffiliateProgramListView(GroupsRequiredMixin, ListView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/affiliate_program_list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = AffiliateProgram
		return context


class AffiliateProgramDetailView(GroupsRequiredMixin, DetailView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/affiliate_program_detail.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']


class AffiliateProgramCreateView(PermsRequiredMixin, CreateView):
	model = AffiliateProgram
	form_class = AffiliateProgramModelForm
	template_name = 'blog/models/affiliate_program/affiliate_program_create.html'
	perms = 'blog.add_affiliateprogram'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class AffiliateProgramUpdateView(PermsRequiredMixin, UpdateView):
	model = AffiliateProgram
	form_class = AffiliateProgramModelForm
	template_name = 'blog/models/affiliate_program/affiliate_program_update.html'
	perms = 'blog.change_affiliateprogram'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class AffiliateProgramDeleteView(PermsRequiredMixin, DeleteView):
	model = AffiliateProgram
	template_name = 'blog/models/affiliate_program/affiliate_program_delete.html'
	perms = 'blog.delete_affiliateprogram'

	def get_success_url(self):
		return AffiliateProgram.get_list_url()


