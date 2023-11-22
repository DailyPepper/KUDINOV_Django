from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination
from rest_framework import generics
import django_filters.rest_framework

class CustomerAPIView(APIView):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()
    def get(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 2)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CustomerSerializer(result_page, many=True)
        return Response(serializer.data)

class ArticlesAPIView(APIView):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Articles.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 2)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ArticlesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

# views.py
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'email']

