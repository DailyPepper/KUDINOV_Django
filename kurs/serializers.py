from rest_framework import serializers
from KUDINOV.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'gender_choices']