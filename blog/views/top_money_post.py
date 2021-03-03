from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from blog.models import TopMoneyPost
from blog.model_forms import TopMoneyPostModelForm
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin
from blog.constants import ACCESS
from django.shortcuts import reverse
User = get_user_model()


class TopMoneyPostDetailView(DetailView):
	model = TopMoneyPost
	template_name = 'blog/models/top_money_post/top_money_post_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class TopMoneyPostCreateView(PermsRequiredMixin, CreateView):
	model = TopMoneyPost
	form_class = TopMoneyPostModelForm
	template_name = 'blog/models/top_money_post/top_money_post_create.html'
	perms = 'blog.add_topmoneypost'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class TopMoneyPostUpdateView(PermsRequiredMixin, UpdateView):
	model = TopMoneyPost
	form_class = TopMoneyPostModelForm
	template_name = 'blog/models/top_money_post/top_money_post_update.html'
	perms = 'blog.change_topmoneypost'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class TopMoneyPostDeleteView(PermsRequiredMixin, DeleteView):
	model = TopMoneyPost
	template_name = 'blog/models/top_money_post/top_money_post_delete.html'
	perms = 'blog.delete_topmoneypost'

	def get_success_url(self):
		return reverse('blog:manage')


