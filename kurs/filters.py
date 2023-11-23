import django_filters
from rest_framework import generics, filters
from KUDINOV.models import Customer, Articles
from .serializers import ArticlesSerializer

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['first_name', 'email']

class ArticlesListView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'price', 'size']
    ordering = ['title']
