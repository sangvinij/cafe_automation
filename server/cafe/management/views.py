from rest_framework import viewsets, permissions
from .models import Menu, Category, CafeAddresses, SocialMediaLinks
from .serializers import MenuSerializer, CategorySerializer, CafeAddressSerializer, LinksSerializer
from .permissions import IsAdminOrReadOnly


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class AddressViewSet(viewsets.ModelViewSet):
    queryset = CafeAddresses.objects.all()
    serializer_class = CafeAddressSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LinksViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaLinks.objects.all()
    serializer_class = LinksSerializer
