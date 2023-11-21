from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, ArticlesSerializer
from KUDINOV.models import Customer, Articles
from .pagination import CustomPageNumberPagination

class CustomerListView(APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPageNumberPagination

class CustomerAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class ArticlesAPIView(APIView):
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Articles.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        page = self.request.query_params.get('page', 1)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ArticlesSerializer(queryset, many=True)
        return Response(serializer.data)
