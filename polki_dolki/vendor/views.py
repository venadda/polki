from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from vendor.Serializer import UserSerializer, CustomerSerializer
from django.contrib.auth.models import User
from vendor.models import Customer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
