from rest_framework import serializers
from .models import Retailer

class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.SlugRelatedField(
        many=True, 
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = Retailer
        fields = ["id","name","vendors"]
