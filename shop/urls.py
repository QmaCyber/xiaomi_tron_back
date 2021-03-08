from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
	path('products/', views.ProductsView.as_view()),
]
