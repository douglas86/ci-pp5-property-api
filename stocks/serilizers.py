from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Stocks


class StockSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    property_address = serializers.CharField()
    property_area = serializers.CharField()
    area_code = serializers.CharField()
    rent = serializers.IntegerField()

    class Meta:
        model = Stocks
        fields = ['id', 'owner', 'property_address', 'property_area', 'area_code', 'rent']
