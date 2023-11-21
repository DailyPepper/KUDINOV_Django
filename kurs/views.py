from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from KUDINOV.models import Customer



class CustomerAPIView(APIView):
    def get(self,request):
        customer = Customer.objects.filter()
        serializer = CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer()