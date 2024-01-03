# api/views.py
from rest_framework import viewsets
from KUDINOV.models import Customer, Articles  # Поправлено на Articles
from .serializers import CustomerSerializer, ArticleSerializer
from django.db.models import Q

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        first_name = self.request.query_params.get('first')
        last_name = self.request.query_params.get('last')
        email = self.request.query_params.get('email')

        if first_name is not None:
            queryset = queryset.filter(first_name__startswith=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name__startswith=last_name)

        if email is not None:
            queryset = queryset.filter(email=email)

        return queryset

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

