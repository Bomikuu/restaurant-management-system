from rest_framework import serializers
from .models import Order
from .models import OrderLine
from django.contrib.auth.models import Group

class OrderSerializer(serializers.ModelSerializer):
    """
    TODO: this
    """
    orderline = OrderLineSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id', 'total_price', 'voided_by', 'cashier', 'status')
    
    def validate(self, *args, **kwargs):


    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        product.save()
        return product


    def update(self, instance, validated_data):
        instance.voided_by = validated_data.get('voided_by', instance.voided_by)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

class OrderLineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderLine
        fields = ('id', 'order', 'product', 'quantity')

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        
        return instance