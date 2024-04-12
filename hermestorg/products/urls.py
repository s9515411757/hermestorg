from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.products, name='products'),
    path("add-rating/", views.add_star_rating, name='add_rating'),
    path('add_products/', views.add_products, name='add_products'),
]
