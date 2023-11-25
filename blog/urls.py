from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('poliplanner.urls')),
    path('professor/', include('django.contrib.auth.urls')),
    path('professor/', include('professor.urls')),
]
