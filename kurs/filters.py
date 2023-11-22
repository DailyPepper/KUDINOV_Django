# filters.py
import django_filters
from KUDINOV.models import Customer

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['first_name', 'email']
