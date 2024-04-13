from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.products, name='products'),
    path("add-rating/", views.add_star_rating, name='add_rating'),
    path('add-products/', views.add_products, name='add_products'),
    path('remove-follow/<str:login>/<int:id>', views.remove_follow, name='remove_follow'),
    path('add-follow/<str:login>/<int:id>', views.add_follow, name='add_follow'),
    path('remove-favourit/<int:pk>/', views.remove_favourit, name='remove_favourit'),
    path('add-favourit/<int:pk>/', views.add_favourit, name='add_favourit'),
]
