from django.urls import path
from . import views


app_name = 'follow'


urlpatterns = [
    path('', views.index, name='index'),
]
