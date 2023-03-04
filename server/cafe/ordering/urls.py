from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'carts', CartViewSet)

cart_router = NestedDefaultRouter(router, r'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')
print(cart_router.urls)

urlpatterns = [
    path(r'api/v1/ordering/', include(router.urls)),
    path(r'api/v1/ordering/', include(cart_router.urls)),
    path(r'api/v1/drf-auth', include('rest_framework.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
]
