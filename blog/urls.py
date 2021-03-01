from django.urls import path
from blog.views import general, category, subcategory, affiliate_program, affiliate_tag

app_name = 'blog'


urlpatterns = [
	path('manage/', general.BlogManage.as_view(), name='manage'),

	# CATEGORY VIEWS
	path('categories/', category.CategoryListView.as_view(), name='category-list'),
	path('category/<int:pk>/subcategories/', category.CategoryDetailListView.as_view(), name='category-detail-list'),
	path('category-create/', category.CategoryCreateView.as_view(), name='category-create'),
	path('category-update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category-update'),
	path('category-delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category-delete'),

	# SUBCATEGORY VIEWS
	path('subcategories/', subcategory.SubCategoryListView.as_view(), name='subcategory-list'),
	path('subcategory/<int:pk>/posts/', subcategory.SubCategoryDetailListView.as_view(), name='subcategory-detail-list'),
	path('subcategory-create/', subcategory.SubCategoryCreateView.as_view(), name='subcategory-create'),
	path('subcategory-update/<int:pk>/', subcategory.SubCategoryUpdateView.as_view(), name='subcategory-update'),
	path('subcategory-delete/<int:pk>/', subcategory.SubCategoryDeleteView.as_view(), name='subcategory-delete'),

	# AFFILIATE PROGRAM VIEWS
	path('affiliate-programs/', affiliate_program.AffiliateProgramListView.as_view(), name='affiliate-program-list'),
	path('affiliate-program/<int:pk>/', affiliate_program.AffiliateProgramDetailView.as_view(), name='affiliate-program-detail'),
	path('affiliate-program-create/', affiliate_program.AffiliateProgramCreateView.as_view(), name='affiliate-program-create'),
	path('affiliate-program-update/<int:pk>/', affiliate_program.AffiliateProgramUpdateView.as_view(), name='affiliate-program-update'),
	path('affiliate-program-delete/<int:pk>/', affiliate_program.AffiliateProgramDeleteView.as_view(), name='affiliate-program-delete'),

	# AFFILIATE TAG VIEWS
	path('affiliate-tags/', affiliate_tag.AffiliateTagListView.as_view(), name='affiliate-tag-list'),
	path('affiliate-tag/<int:pk>/', affiliate_tag.AffiliateTagDetailView.as_view(), name='affiliate-tag-detail'),
	path('affiliate-tag-create/', affiliate_tag.AffiliateTagCreateView.as_view(), name='affiliate-tag-create'),
	path('affiliate-tag-update/<int:pk>/', affiliate_tag.AffiliateTagUpdateView.as_view(), name='affiliate-tag-update'),
	path('affiliate-tag-delete/<int:pk>/', affiliate_tag.AffiliateTagDeleteView.as_view(), name='affiliate-tag-delete'),

]
