from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
	path('products/', views.ProductsView.as_view()),
	path('products/<str:categorySlug>', views.CategoryView.as_view()),
	path('product/<str:productSlug>', views.ProductView.as_view()),
	path('popularproducts/', views.PopularProductsView.as_view()),
	path('sliders/', views.SlidersView.as_view()),
	path('search/<str:text>', views.SearchView.as_view()),
	path('news/', views.NewsView.as_view()),
	path('news/<str:newsSlug>', views.NewsView.as_view()),
	path('reviews/', views.ReviewsView.as_view()),
	path('auth', views.LoginView.as_view()),
	path('authme', views.AuthView),
	path('reg', views.ResiterView.as_view()),
]

