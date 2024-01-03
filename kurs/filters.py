import django_filters
from rest_framework import generics, filters, renderers
from KUDINOV.models import Customer, Articles
from .serializers import ArticlesSerializer

class NumericRangeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_value = request.query_params.get('min_value')
        max_value = request.query_params.get('max_value')
        if min_value and max_value:
            return queryset.filter(numeric_field__range=[min_value, max_value])
        return queryset

class SpecificFieldFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        specific_value = request.query_params.get('specific_field')
        if specific_value:
            return queryset.filter(specific_field=specific_value)
        return queryset

class ChoiceFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        selected_option = request.query_params.get('selected_option')
        if selected_option:
            return queryset.filter(choice_field=selected_option)
        return queryset

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)