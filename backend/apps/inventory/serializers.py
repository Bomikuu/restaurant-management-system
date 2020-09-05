from rest_framework import serializers
from .models import InventoryItem, InventoryItemLog


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

    def create(self, validated_data):
        product = InventoryItem(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance


class InventoryItemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItemLog
        fields = '__all__'

    def create(self, validated_data):
        product = InventoryItemLog(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.timestamp = validated_data.get('status', instance.timestamp)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.log_type = validated_data.get('log_type', instance.log_type)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.save()

        return instance