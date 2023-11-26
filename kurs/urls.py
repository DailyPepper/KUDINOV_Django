from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from kurs import settings
from . import views
from rest_framework import routers, serializers, viewsets
from .views import CustomerAPIView
from .views import ArticlesViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerAPIView, basename='customer')
router.register(r'articles', ArticlesViewSet, basename='articles')

app_name = "KUDINOV"
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('KUDINOV.urls')),
                  path('api-auth/', include('rest_framework.urls'), name='api-auth'),
                  path('api/', include(router.urls)),
                  # path('api/', include('api.urls', namespace='api')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
