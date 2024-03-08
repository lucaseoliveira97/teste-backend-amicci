from django.shortcuts import render
from rest_framework import generics
from .models import Briefing
from .serializers import BriefingSerializer

class BriefingsListView (generics.ListAPIView):
    queryset=Briefing.objects.all()
    serializer_class=BriefingSerializer

class BriefingCreateView (generics.CreateAPIView):
    queryset=Briefing.objects.all()
    serializer_class=BriefingSerializer

class BriefingRetrieveUpdateView (generics.RetrieveUpdateAPIView):
    queryset=Briefing.objects.all()
    serializer_class=BriefingSerializer
    http_method_names = ["get","put", "post"]


