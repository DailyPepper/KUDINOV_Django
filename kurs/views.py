from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from .filters import IsOwnerFilterBackend
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination
from rest_framework import generics
import django_filters.rest_framework
from django.db.models import Q

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
        return paginator.get_paginated_response(serializer.data)

        @api_view(['GET'])
        def filter_user(request):
            first__name = self.request.query_params.get('first')
            last__name = self.request.query_params.get('last')
            emails = self.request.query_params.get('email')

            queryset = Customer.objects.filter(
                Q(username__startswith='first__name') & ~Q(username__startswith='last__name') | Q(username__startswith='emails')
            )
            serializer = CustomerSerializer(queryset, many=True)
            return Response(serializer.data)

        filtered_customers = Customer.objects.filter(q_filter)

        # Вывод результатов
        for customer in filtered_customers:
            print(customer.username)
class ArticlesAPIView(APIView):
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['title', 'price', 'size']
    permission_classes = (IsOwnerFilterBackend)
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

