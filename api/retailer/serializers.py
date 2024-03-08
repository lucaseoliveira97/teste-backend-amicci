from rest_framework import serializers

from vendor.models import Vendor
from .models import Retailer

class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.SlugRelatedField(
        many=True, 
        read_only=False,
        queryset=Vendor.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = Retailer
        fields = ["id","name","vendors"]
