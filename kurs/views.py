from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination


def Q(username__startswith):
    pass


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

    @action(detail=False, methods=['GET'])
    def filter_user(self, request):
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        email = self.request.query_params.get('email')

        queryset = Customer.objects.filter(
            Q(username__startswith=first_name) & ~Q(username__startswith=last_name) | Q(username__startswith=email)
        )

        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_all_customers(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def create_customer(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SearchFilter:
    pass


class OrderingFilter:
    pass


class ArticlesAPIView(APIView):
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['title', 'price', 'size']

    def get_queryset(self):
        return Articles.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 2)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ArticlesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_article(self, request):
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
