from rest_framework  import serializers 
from Products.models import Aksesuar, Products
from datetime import datetime, date

class AksesuarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aksesuar
        fields = '__all__'
        read_only_fields = ['id','create_date','update_date']

class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Products
        fields = '__all__'
        read_only_fields = ['id','create_date','update_date']
        
        