# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'articles', ArticleViewSet, basename='article')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),

]
