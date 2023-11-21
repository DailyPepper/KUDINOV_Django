from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer
from KUDINOV.models import Articles



class CustomerAPIView(APIView):
    def get(self,request):
        customer = Customer.objects.filter()
        serializer = CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer()

class ArticlesAPIView(APIView):
    def get(self, request):
        articles = Articles.objects.filter()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    queryset = Articles.objects.all()
    serializers_class = ArticlesSerializer()