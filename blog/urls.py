from django.urls import path
from blog.views import category

app_name = 'blog'
urlpatterns = [
	path('categories/', category.CategoryListView.as_view(), name='category-list'),
	path('category/<int:pk>/', category.CategoryDetailView.as_view(), name='category-detail'),
	path('category-create/', category.CategoryCreateView.as_view(), name='category-create'),
	path('category-update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category-update'),
	path('category-delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category-delete'),
]
