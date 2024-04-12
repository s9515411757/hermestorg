from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('auth/', include('users.urls', namespace='users')),
    path('products/', include('products.urls', namespace='products')),
    path('about/', include('about.urls', namespace='about')),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+= static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )