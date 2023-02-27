from django.urls import include, path
from .views import MenuViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
print(router.urls)

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('api/v1/menulist/', MenuViewSet.as_view({'get': 'list'})),
    # path('api/v1/menulist/<int:pk>/', MenuViewSet.as_view({'put': 'update'}))
]
