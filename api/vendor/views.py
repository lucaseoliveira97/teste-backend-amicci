from django.shortcuts import render
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer

class VendorsListView (generics.ListAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class VendorCreateView (generics.CreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class VendorRetrieveUpdateView (generics.RetrieveUpdateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    http_method_names = ["get","put", "post"]


