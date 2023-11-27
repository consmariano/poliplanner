from django.contrib import admin
from django.urls import path, include

from .views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("professor/", include("professor.urls")),
    path("", include("calendarapp.urls")),
]