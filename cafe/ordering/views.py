from management.permissions import IsAdminOrReadOnly

from rest_framework.mixins import CreateModelMixin, \
    DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Cart, CartItems, OrderStatus, PaymentType
from .serializers import AddCartItemSerializer, CartItemSerializer, \
                        CartSerializer, OrderSerializer, \
                        OrderStatusSerializer, \
                        PaymentTypeSerializer, UpdateCartItemSerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin,
                  DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs['cart_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer

        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer

        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}


class OrderViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = OrderSerializer


class PaymentTypeViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class OrderStatusViewSet(ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = (IsAdminOrReadOnly,)
