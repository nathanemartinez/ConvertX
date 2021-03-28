from django.views.generic import TemplateView
from blog.mixins import GroupsRequiredMixin
from blog.constants import ACCESS
from blog.models import Category, SubCategory, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct


class BlogManage(GroupsRequiredMixin, TemplateView):
	template_name = 'blog/general/manage.html'
	groups = ACCESS['MANAGE']
	extra_context = {
		'models': [Category, SubCategory, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct]
	}
