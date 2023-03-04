from django.urls import include, path
from .views import MenuViewSet, CategoryViewSet, AddressViewSet, LinksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'menu_categories', CategoryViewSet)
router.register(r'cafe_addresses', AddressViewSet)
router.register(r'social_media_links', LinksViewSet)
print(router.urls)

urlpatterns = [
    path('api/v1/management/', include(router.urls))
]
