from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
	path('products/', views.ProductsView.as_view()),
	path('products/<str:categorySlug>', views.CategoryView.as_view()),
	path('product/<str:productSlug>', views.ProductView.as_view()),
	path('popularproducts/', views.popularProductsView.as_view()),
<<<<<<< HEAD
	path('slader/', views.slider.as_view())
]
=======
	path('search/<str:text>', views.SearchView.as_view())
]

>>>>>>> 463e93f70aea92dee839647aff14fa5071699ba0
