from rest_framework import serializers
from waiters.models import Waiter, Restaurant


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['id', 'name', 'surname']


class RestaurantSerializer(serializers.ModelSerializer):
    waiters = WaiterSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'waiters']
