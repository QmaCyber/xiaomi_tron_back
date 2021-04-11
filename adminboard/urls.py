from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
	path('products/', views.ProductsView.as_view()),
	path('products/<str:categorySlug>', views.ProductCategoryView.as_view()),
	path('categorys', views.CategoryView.as_view()),
	path('product/<str:productSlug>', views.ProductView.as_view()),
	path('popularproducts/', views.PopularProductsView.as_view()),
	path('slides/', views.SlidesView.as_view()),
	path('search/<str:text>', views.SearchView.as_view()),
	path('news/', views.NewsView.as_view()),
	path('reviews/', views.ReviewsView.as_view()),
]
