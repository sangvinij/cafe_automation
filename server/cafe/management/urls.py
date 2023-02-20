from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('api/v1/menulist', MenuAPIView.as_view())
]
