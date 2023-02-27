from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Menu, Category
from .serializers import MenuSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrReadOnly, )

    @action(methods=['get', 'post'], detail=False)
    def list_of_categories(self, request):
        categories = Category.objects.all()
        return Response({'categories': [category.category_name for category in categories]})

    @action(methods=['get', 'put', 'delete'], detail=True)
    def one_category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        return Response({'categories': category.category_name})
# class MenuAPIView(generics.ListAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#
#
# class MenuAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
