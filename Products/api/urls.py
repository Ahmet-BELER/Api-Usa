from django.urls import path, include
from rest_framework import routers
from .views import AksesuarViewSet, ProductsViewSet, CashTypeCreateViewSet

router = routers.DefaultRouter()
router.register('aksesuar', AksesuarViewSet)
router.register('product', ProductsViewSet)
router.register('cash-type', CashTypeCreateViewSet) # Yeni eşleştirme

urlpatterns = [
    path('', include(router.urls)),
]
