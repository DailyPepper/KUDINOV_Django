
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from kurs import settings

app_name = "KUDINOV"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KUDINOV.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

