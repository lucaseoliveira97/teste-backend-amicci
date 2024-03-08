from rest_framework import serializers
from retailer.models import Retailer
from category.models import Category
from .models import Briefing

class BriefingSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False, 
        read_only=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )
    retailer = serializers.SlugRelatedField(
        many=False, 
        read_only=False,
        queryset=Retailer.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = Briefing
        fields = ["id","name","retailer","responsible","category","release_date","availabe"]
