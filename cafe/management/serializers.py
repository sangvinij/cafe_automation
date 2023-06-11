from rest_framework import serializers

from .models import CafeAddresses, Category, Menu, SocialMediaLinks


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', )


class MenuSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.category")

    class Meta:
        model = Menu
        fields = ('title', 'price', 'image', 'category')


class AddMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CafeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CafeAddresses
        fields = ('cafe_address',)


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = ('social_media_name', 'social_media_link')
