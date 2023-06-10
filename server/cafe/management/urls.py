from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework import routers

from .views import AddressViewSet, CategoryViewSet, LinksViewSet, MenuViewSet


router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'menu_categories', CategoryViewSet)
router.register(r'cafe_addresses', AddressViewSet)
router.register(r'social_media_links', LinksViewSet)
# print(router.urls)

urlpatterns = [
    path('api/v1/management/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
