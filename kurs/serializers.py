from rest_framework import serializers
from KUDINOV.models import Customer
from KUDINOV.models import Articles

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'gender_choices']

class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ['title','price', 'size','date']





