from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from blog.models import TopMoneyProduct
from blog.model_forms import TopMoneyProductModelForm
from django.contrib.auth import get_user_model
from blog.mixins import PermsRequiredMixin
from blog.constants import ACCESS
from django.shortcuts import reverse
User = get_user_model()


class TopMoneyProductDetailView(PermsRequiredMixin, DetailView):
	model = TopMoneyProduct
	template_name = 'blog/models/top_money_product/top_money_product_detail.html'
	perms = 'blog.view_topmoneyproduct'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = User.in_groups(ACCESS['MANAGE'], self.request.user)
		return context


class TopMoneyProductCreateView(PermsRequiredMixin, CreateView):
	model = TopMoneyProduct
	form_class = TopMoneyProductModelForm
	template_name = 'blog/models/top_money_product/top_money_product_create.html'
	perms = 'blog.add_topmoneyproduct'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)


class TopMoneyProductUpdateView(PermsRequiredMixin, UpdateView):
	model = TopMoneyProduct
	form_class = TopMoneyProductModelForm
	template_name = 'blog/models/top_money_product/top_money_product_update.html'
	perms = 'blog.change_topmoneyproduct'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)


class TopMoneyProductDeleteView(PermsRequiredMixin, DeleteView):
	model = TopMoneyProduct
	template_name = 'blog/models/top_money_product/top_money_product_delete.html'
	perms = 'blog.delete_topmoneyproduct'

	def get_success_url(self):
		return reverse('blog:manage')


