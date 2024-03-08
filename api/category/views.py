from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoriesListView (generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryCreateView (generics.CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryRetrieveUpdateView (generics.RetrieveUpdateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


