from django.urls import path, include

from .views import WaiterListViewSet, RestaurantListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('waiters', WaiterListViewSet)
router.register('restaurants', RestaurantListViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
