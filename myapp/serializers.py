from django.contrib.auth import authenticate
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'
        # extera_kwargs = {'password':{'read_only': True},'is_admin':{'read_only': True},'is_active':{'read_only': True}} #غیرقابل دسترسی توسط کلاینت 


# class SafeUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.UserModel
#         fields = ('usera_name', 'first_name', 'last_name')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopModel
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BranchModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckModel
        fields = '__all__'


class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstallmentModel 
        fields = '__all__'