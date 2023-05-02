from django.urls import path
from .views import AksesuarListCreateView,ProductListCreateView,AksesuarDetailView,ProductDetailView 


urlpatterns = [
    
    path('aksesuar/', AksesuarListCreateView.as_view(),name="aksesuar_list_create" ),
    path('product/', ProductListCreateView.as_view(), name="product_list_create"),
    path('aksesuar/<int:id>', AksesuarDetailView.as_view(), name="aksesuar_detail"),
    path('product/<int:id>', ProductDetailView.as_view(), name="product_detail"),
    
]
