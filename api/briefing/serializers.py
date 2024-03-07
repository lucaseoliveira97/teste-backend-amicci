from rest_framework import serializers
from .models import Briefing

class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = ["id","name","retailer","responsible","category","release_date","availabe"]
