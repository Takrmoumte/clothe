from rest_framework import serializers
from . import models

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

class VendorDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=models.Vendor
        fields=['id','user','address']


