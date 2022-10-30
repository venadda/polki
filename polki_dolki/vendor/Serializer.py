from rest_framework import serializers
from django.contrib.auth.models import User
from vendor.models import Customer, VendorRegistration


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'cust_firstname', 'cust_lastname', 'cust_email', 'cust_phone', 'cust_status']


class VendorRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendorRegistration
        fields = ['id', 'cust_firstname', 'cust_lastname', 'cust_email', 'cust_phone', 'cust_status']
