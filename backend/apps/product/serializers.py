from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import Group

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('name', 'price', 'status', 'description')

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance