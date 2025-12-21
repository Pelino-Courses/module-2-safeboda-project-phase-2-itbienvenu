from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TripViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
