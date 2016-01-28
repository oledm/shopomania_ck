from rest_framework import serializers
from .models import Order, Item, Customer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer


class ItemSerializer(serializers.ModelSerializer):
    order = serializers.SlugRelatedField(read_only=True, slug_field='date')
    customer = serializers.SlugRelatedField(read_only=True, slug_field='fio')

    class Meta:
        model = Item

