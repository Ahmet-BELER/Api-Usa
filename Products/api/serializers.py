from rest_framework import serializers
from Products.models import Aksesuar, Products, CashTypeCreate

class AksesuarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aksesuar
        fields = '__all__'
        
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class CashTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTypeCreate
        fields = '__all__'
