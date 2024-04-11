from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
