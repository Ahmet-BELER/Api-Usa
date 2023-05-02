from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from Products.models import Aksesuar, Products
from .serializers import AksesuarSerializer, ProductsSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import permissions 

 
 
 


class AksesuarListCreateView(APIView):
    def get(self,request):
        aksesuar = Aksesuar.objects.all()
        serializer = AksesuarSerializer(aksesuar, many=True, context={'request': request})
        return Response(serializer.data)
  
    
    def post(self,request):
       
        serializer = AksesuarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
      
class ProductListCreateView(APIView):
    def get(self,request):
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many=True, context={'request': request})   
        return Response(serializer.data)
    
    def post (self,request):
        serializer =ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]        

class AksesuarDetailView(APIView):
    
    def get_objects(self,id):
        aksesuar_instance = get_object_or_404(Aksesuar, id=id)
        return aksesuar_instance
    
    def get(self,request,id):
        aksesuar = self.get_objects(id=id)
        serializer= AksesuarSerializer(aksesuar)
        return Response(serializer.data)
    
    def put(self,request,id):
        aksesuar = self.get_object(id=id)
        serializer= AksesuarSerializer(aksesuar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        aksesuar=self.get_object(id=id)
        aksesuar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
class ProductDetailView(APIView):
    
    def get_objects(self,id):
        product_instance = get_object_or_404(Products,id=id) 
        return product_instance
    
    def get(self,request,id):
        
        product = self.get_objects(id=id)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    def put(self,request,id):  
        product = self.get_object(id=id)
        serializer = ProductsSerializer(product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, id):
        product = self.get_object(id=id)   
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 