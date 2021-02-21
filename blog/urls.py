from django.urls import path
from blog.views import category
from blog.views import general

app_name = 'blog'
urlpatterns = [
	path('manage/', general.BlogManage.as_view(), name='manage'),

	path('manage/categories/', category.CategoryListView.as_view(), name='category-list'),
	path('category/<int:pk>/subcategories/', category.CategoryDetailListView.as_view(), name='category-detail-list'),
	path('category/<int:pk>/', category.CategoryDetailView.as_view(), name='category-detail'),
	path('manage/category-create/', category.CategoryCreateView.as_view(), name='category-create'),
	path('manage/category-update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category-update'),
	path('manage/category-delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category-delete'),
]
