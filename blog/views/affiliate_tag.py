from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from blog.models import AffiliateTag
from blog.model_forms import AffiliateTagModelForm
from blog.constants import PAG_BY, ACCESS
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
User = get_user_model()


class AffiliateTagListView(GroupsRequiredMixin, ListView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/affiliate_tag_list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = self.model
		return context


class AffiliateTagDetailView(GroupsRequiredMixin, DetailView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/affiliate_tag_detail.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']


class AffiliateTagCreateView(PermsRequiredMixin, CreateView):
	model = AffiliateTag
	form_class = AffiliateTagModelForm
	template_name = 'blog/models/affiliate_tag/affiliate_tag_create.html'
	perms = 'blog.add_affiliatetag'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class AffiliateTagUpdateView(PermsRequiredMixin, UpdateView):
	model = AffiliateTag
	form_class = AffiliateTagModelForm
	template_name = 'blog/models/affiliate_tag/affiliate_tag_update.html'
	perms = 'blog.change_affiliatetag'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class AffiliateTagDeleteView(PermsRequiredMixin, DeleteView):
	model = AffiliateTag
	template_name = 'blog/models/affiliate_tag/affiliate_tag_delete.html'
	perms = 'blog.delete_affiliatetag'

	def get_success_url(self):
		return self.model.get_list_url()


