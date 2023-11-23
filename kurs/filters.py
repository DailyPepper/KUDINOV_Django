import django_filters
from rest_framework import generics, filters, renderers
from KUDINOV.models import Customer, Articles
from .serializers import ArticlesSerializer

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)