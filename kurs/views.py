from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination
from rest_framework import generics, filters
import django_filters.rest_framework
from django.db.models import Q


class CustomerAPIView(ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['first_name', 'last_name', 'email']

    @action(detail=False, methods=['GET'])
    def filter_user(self, request):
        first_name = request.query_params.get('first')
        last_name = request.query_params.get('last')
        emails = request.query_params.get('email')

        queryset = Customer.objects.filter(
            Q(first_name__startswith=first_name) & ~Q(last_name__startswith=last_name) | Q(email__startswith=emails)
        )
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def custom_action_post(self, request, pk=None):
        customer = self.get_object()
        data = {'message': 'Custom action for POST method', 'customer_id': customer.id}
        serializer = self.get_serializer(data)
        return Response(serializer.data)


class ArticlesViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'price', 'size']
    serializer_class = ArticlesSerializer
    filterset_fields = ('title', 'size')
    search_fields = ('title',)


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