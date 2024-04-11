from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('auth/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
