

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("otlk/", include('otlk_micro.urls'))
]
