from rest_framework import serializers
from KUDINOV.models import Customer, Articles


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'price', 'size', 'date')

    def validate_title(self, value):
        if Articles.objects.filter(title=value).exists():
            raise serializers.ValidationError('Продукт с таким названием уже существует.')
        return value

    def validate_price(self, value):
        if value > 0:
            raise serializers.ValidationError('Цена должна быть больше 0')
        return value

    title = serializers.CharField(validators=[validate_title])
    price = serializers.CharField(validators=[validate_price])