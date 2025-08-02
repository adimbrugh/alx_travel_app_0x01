

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'listing', ListingViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'reviews', ReviewViewSet)  # Added ReviewViewSet


urlpatterns = [
    path('', include(router.urls)),
]
