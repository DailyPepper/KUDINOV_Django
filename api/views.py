# api/views.py
from rest_framework import viewsets
from KUDINOV.models import Customer, Articles  # Поправлено на Articles
from .serializers import CustomerSerializer, ArticleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
