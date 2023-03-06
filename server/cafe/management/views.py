from rest_framework import viewsets

from .models import CafeAddresses, Category, Menu, SocialMediaLinks
from .permissions import IsAdminOrReadOnly
from .serializers import AddMenuSerializer, CafeAddressSerializer, \
    CategorySerializer, LinksSerializer, MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddMenuSerializer

        return MenuSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = CafeAddresses.objects.all()
    serializer_class = CafeAddressSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LinksViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaLinks.objects.all()
    serializer_class = LinksSerializer
    permission_classes = (IsAdminOrReadOnly,)
