from django.contrib.auth import get_user_model, get_user
from djoser.serializers import UserSerializer

from rest_framework import serializers

from .models import Cart, CartItems, User
from management.models import Menu


class CurrentUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'email')


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', ]


class CartMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    item = CartMenuSerializer()
    cart_item_price = serializers.SerializerMethodField(method_name='total_price_of_one_cart_item')

    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'item', 'amount', 'cart_item_price']

    @staticmethod
    def total_price_of_one_cart_item(cart_item: CartItems):
        return round(cart_item.amount * cart_item.item.price, 2)


class AddCartItemSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()

    @staticmethod
    def validate_item_id(pk):
        if not Menu.objects.filter(pk=pk).exists():
            raise serializers.ValidationError('Такого item_id не существует')
        return pk

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        item_id = self.validated_data['item_id']
        amount = self.validated_data['amount']

        try:
            cart_item = CartItems.objects.get(item_id=item_id, cart_id=cart_id)
            cart_item.amount += amount
            cart_item.save()

            self.instance = cart_item

        except:
            self.instance = CartItems.objects.create(item_id=item_id, cart_id=cart_id, amount=amount)
        return self.instance

    class Meta:
        model = CartItems
        fields = ['id', 'item_id', 'amount']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['amount']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    carts = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='price_of_whole_cart')

    class Meta:
        model = Cart
        fields = ['id', 'carts', 'total_price']

    @staticmethod
    def price_of_whole_cart(cart: Cart):
        items = cart.carts.all()
        total_price = round(sum([cart_item.amount * cart_item.item.price for cart_item in items]), 2)
        return total_price



