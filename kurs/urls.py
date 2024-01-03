from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from kurs import settings
from . import views
from rest_framework import routers, serializers, viewsets
from .views import CustomerAPIView
from .views import ArticlesAPIView



app_name = "KUDINOV"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KUDINOV.urls')),
    path('api-auth/', include('rest_framework.urls'), name='api-auth'),
    path('customer/', CustomerAPIView.as_view(), name='customer-api-view'),
    path('customer/filter_user/', CustomerAPIView.filter_user, name='customer-filter-user'),
    path('customer/get_all_customers/', CustomerAPIView.get_all_customers, name='customer-get-all-customers'),
    path('customer/create_customer/', CustomerAPIView.create_customer, name='customer-create-customer'),
    path('articles/', ArticlesAPIView.as_view(), name='articles-api-view'),
    path('articles/create_article/', ArticlesAPIView.create_article, name='articles-create-article'),
    path('api/', include('api.urls', namespace='api')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

