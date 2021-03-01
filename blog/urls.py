from django.urls import path
from blog.views import general, category, subcategory

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

]
