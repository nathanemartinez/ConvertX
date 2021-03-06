from django.urls import path
from blog.views import general, category, subcategory, affiliate_program, affiliate_tag, top_money_post, top_money_product

app_name = 'blog'
urlpatterns = [
	path('manage/', general.BlogManage.as_view(), name='manage'),

	# CATEGORY URLS
	path('categories/', category.CategoryListView.as_view(), name='category-list'),
	path('category/<int:pk>/subcategories/', category.CategoryDetailListView.as_view(), name='category-detail-list'),
	path('category-create/', category.CategoryCreateView.as_view(), name='category-create'),
	path('category-update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category-update'),
	path('category-delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category-delete'),

	# SUBCATEGORY URLS
	path('subcategories/', subcategory.SubCategoryListView.as_view(), name='subcategory-list'),
	path('subcategory/<int:pk>/posts/', subcategory.SubCategoryDetailListView.as_view(), name='subcategory-detail-list'),
	path('subcategory-create/', subcategory.SubCategoryCreateView.as_view(), name='subcategory-create'),
	path('subcategory-update/<int:pk>/', subcategory.SubCategoryUpdateView.as_view(), name='subcategory-update'),
	path('subcategory-delete/<int:pk>/', subcategory.SubCategoryDeleteView.as_view(), name='subcategory-delete'),

	# AFFILIATE PROGRAM URLS
	path('affiliate-programs/', affiliate_program.AffiliateProgramListView.as_view(), name='affiliate-program-list'),
	path('affiliate-program/<int:pk>/', affiliate_program.AffiliateProgramDetailView.as_view(), name='affiliate-program-detail'),
	path('affiliate-program-create/', affiliate_program.AffiliateProgramCreateView.as_view(), name='affiliate-program-create'),
	path('affiliate-program-update/<int:pk>/', affiliate_program.AffiliateProgramUpdateView.as_view(), name='affiliate-program-update'),
	path('affiliate-program-delete/<int:pk>/', affiliate_program.AffiliateProgramDeleteView.as_view(), name='affiliate-program-delete'),

	# AFFILIATE TAG URLS
	path('affiliate-tags/', affiliate_tag.AffiliateTagListView.as_view(), name='affiliate-tag-list'),
	path('affiliate-tag/<int:pk>/', affiliate_tag.AffiliateTagDetailView.as_view(), name='affiliate-tag-detail'),
	path('affiliate-tag-create/', affiliate_tag.AffiliateTagCreateView.as_view(), name='affiliate-tag-create'),
	path('affiliate-tag-update/<int:pk>/', affiliate_tag.AffiliateTagUpdateView.as_view(), name='affiliate-tag-update'),
	path('affiliate-tag-delete/<int:pk>/', affiliate_tag.AffiliateTagDeleteView.as_view(), name='affiliate-tag-delete'),

	# TOP MONEY POST URLS
	path('top-money-post/<int:pk>/', top_money_post.TopMoneyPostListDetailView.as_view(), name='top-money-post-list-detail'),
	path('<int:pk>/<slug:slug>/', top_money_post.TopMoneyPostDetailView.as_view(), name='top-money-post-detail'),
	path('top-money-post-create/', top_money_post.TopMoneyPostCreateView.as_view(), name='top-money-post-create'),
	path('top-money-post-update/<int:pk>/', top_money_post.TopMoneyPostUpdateView.as_view(), name='top-money-post-update'),
	path('top-money-post-delete/<int:pk>/', top_money_post.TopMoneyPostDeleteView.as_view(), name='top-money-post-delete'),

	# TOP MONEY PRODUCT URLS
	path('top-money-product/<int:pk>/', top_money_product.TopMoneyProductDetailView.as_view(), name='top-money-product-detail'),
	path('top-money-product-create/', top_money_product.TopMoneyProductCreateView.as_view(), name='top-money-product-create'),
	path('top-money-product-update/<int:pk>/', top_money_product.TopMoneyProductUpdateView.as_view(), name='top-money-product-update'),
	path('top-money-product-delete/<int:pk>/', top_money_product.TopMoneyProductDeleteView.as_view(), name='top-money-product-delete'),

]

