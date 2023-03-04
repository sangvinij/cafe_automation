from rest_framework import serializers
from .models import Menu, Category, CafeAddresses, SocialMediaLinks


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)


class CafeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CafeAddresses
        fields = ('cafe_address',)


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = ('social_media_name', 'social_media_link')
