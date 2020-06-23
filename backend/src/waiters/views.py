from django.shortcuts import render

from rest_framework import viewsets
from waiters.models import Waiter, Restaurant
from .serializers import WaiterSerializer, RestaurantSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class RestaurantListViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = (TokenAuthentication,)


class WaiterListViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    authentication_classes = (TokenAuthentication,)
#    permission_classes = (AllowAny,)
