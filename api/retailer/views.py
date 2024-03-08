from django.shortcuts import render
from rest_framework import generics
from .models import Retailer
from .serializers import RetailerSerializer

class RetailersListView (generics.ListAPIView):
    queryset=Retailer.objects.all()
    serializer_class=RetailerSerializer

class RetailerCreateView (generics.CreateAPIView):
    queryset=Retailer.objects.all()
    serializer_class=RetailerSerializer

class RetailerRetrieveUpdateView (generics.RetrieveUpdateAPIView):
    queryset=Retailer.objects.all()
    serializer_class=RetailerSerializer
    http_method_names = ["get","put", "post"]




