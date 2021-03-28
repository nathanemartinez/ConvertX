from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from blog.models import TopMoneyPost
from blog.forms import TopMoneyPostModelForm
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
from blog.constants import ACCESS, PAG_BY
from django.shortcuts import reverse
User = get_user_model()


class TopMoneyPostListDetailView(GroupsRequiredMixin, DetailView, MultipleObjectMixin):
	model = TopMoneyPost
	template_name = 'blog/models/top_money_post/detail_list.html'
	paginate_by = PAG_BY
	groups = ACCESS['MANAGE']

	def get_context_data(self, **kwargs):
		object_list = self.object.get_topmoneyproducts()
		context = super().get_context_data(object_list=object_list, **kwargs)
		context['status'] = TopMoneyPost.get_choice_display(self.object.status)
		return context


class TopMoneyPostDetailView(DetailView):
	model = TopMoneyPost
	template_name = 'blog/models/top_money_post/detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		context['object_list'] = self.object.get_topmoneyproducts()
		return context


class TopMoneyPostCreateView(PermsRequiredMixin, CreateView):
	model = TopMoneyPost
	form_class = TopMoneyPostModelForm
	template_name = 'blog/models/top_money_post/create.html'
	perms = 'blog.add_topmoneypost'
	extra_context = {
		'obj': TopMoneyPost,
		'tmp_post_create': True,
	}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TopMoneyPostUpdateView(PermsRequiredMixin, UpdateView):
	model = TopMoneyPost
	form_class = TopMoneyPostModelForm
	template_name = 'blog/models/top_money_post/update.html'
	perms = 'blog.change_topmoneypost'
	extra_context = {
		'obj': TopMoneyPost,
		'tmp_post_update': True,
	}

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TopMoneyPostDeleteView(PermsRequiredMixin, DeleteView):
	model = TopMoneyPost
	template_name = 'blog/models/top_money_post/delete.html'
	perms = 'blog.delete_topmoneypost'
	extra_context = {
		'obj': TopMoneyPost
	}

	def get_success_url(self):
		return reverse('blog:manage')
