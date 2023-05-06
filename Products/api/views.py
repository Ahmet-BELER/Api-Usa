from rest_framework import viewsets
from rest_framework.response import Response
from Products.models import Aksesuar, Products, CashTypeCreate
from .serializers import AksesuarSerializer, ProductsSerializer, CashTypeCreateSerializer

class AksesuarViewSet(viewsets.ModelViewSet):
    queryset = Aksesuar.objects.all()
    serializer_class = AksesuarSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CashTypeCreateViewSet(viewsets.ModelViewSet):
    queryset = CashTypeCreate.objects.all()
    serializer_class = CashTypeCreateSerializer
