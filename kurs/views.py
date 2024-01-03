from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .filters import IsOwnerFilterBackend
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination
from rest_framework import generics, filters
import django_filters.rest_framework
from django.db.models import Q

class CustomerAPIView(viewsets.ViewSet):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 5)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def filter_user(self, request):
        first_name = request.query_params.get('first')
        last_name = request.query_params.get('last')
        emails = request.query_params.get('email')

        queryset = Customer.objects.filter(
            Q(username__startswith=first_name) & ~Q(username__startswith=last_name) | Q(username__startswith=emails)
        )
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def filter_user(request):
    first_name = request.query_params.get('first')
    last_name = request.query_params.get('last')
    emails = request.query_params.get('email')

    queryset = Customer.objects.filter(
        Q(username__startswith=first_name) & ~Q(username__startswith=last_name) | Q(username__startswith=emails)
    )
    serializer = CustomerSerializer(queryset, many=True)
    return Response(serializer.data)

class ArticlesViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    # pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'price', 'size']
    serializer_class = ArticlesSerializer
    filterset_fields = ('title', 'size')
    search_fields = ('title',)  # Note the parentheses

    # Uncomment this if you want to enable pagination
    # def get(self, request):
    #     queryset = self.get_queryset()
    #     page = self.request.query_params.get('page', 2)
    #     paginator = self.pagination_class()
    #     result_page = paginator.paginate_queryset(queryset, request)
    #     serializer = ArticlesSerializer(result_page, many=True)
    #     return paginator.get_paginated_response(serializer.data)

# views.py
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'email']

    def filter_user(self, request):
        first_name = request.query_params.get('first')
        last_name = request.query_params.get('last')
        emails = request.query_params.get('email')

        queryset = Customer.objects.filter(
            Q(username__startswith=first_name) & ~Q(username__startswith=last_name) | Q(username__startswith=emails)
        ).distinct()

        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)