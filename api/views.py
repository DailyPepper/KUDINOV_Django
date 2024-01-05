from KUDINOV.models import Customer
from kurs.pagination import CustomPageNumberPagination
from KUDINOV.serializers import CustomerSerializer, ArticleSerializer
from rest_framework import viewsets
from KUDINOV.models import Articles
from rest_framework.response import Response
from rest_framework import status


class CustomerAPIView(viewsets.ViewSet):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        self.request.query_params.get('page', 4)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
