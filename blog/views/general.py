from django.views.generic import TemplateView
from blog.mixins import PermsRequiredMixin, GroupsRequiredMixin
from blog.constants import ACCESS_GROUPS
from blog.models import Category, Tag, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct

class BlogManage(GroupsRequiredMixin, TemplateView):
	template_name = 'blog/general/manage.html'
	groups = ACCESS_GROUPS

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['models'] = [Category, Tag, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct]
		return data
