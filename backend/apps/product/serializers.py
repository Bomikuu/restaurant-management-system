from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import Group

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('name','price','status','desscription')

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = Account(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     UserProfile.objects.create(user=user)
    #     return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     return instance