# api/views.py
from rest_framework import viewsets
from KUDINOV.models import Customer, Articles  # Поправлено на Articles
from .serializers import CustomerSerializer, ArticleSerializer
from .pagination import CustomPageNumberPagination
from django.db.models import Q


class CustomerAPIView(viewsets.ViewSet):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 2)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
