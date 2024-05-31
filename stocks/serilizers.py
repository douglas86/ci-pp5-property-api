from rest_framework import serializers
from .models import Stocks


class StockSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    property_image = serializers.ImageField()
    property_address = serializers.CharField()
    property_area = serializers.CharField()
    area_code = serializers.CharField()
    rent = serializers.IntegerField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Stocks
        fields = ['id', 'owner', 'is_owner', 'property_image', 'property_address', 'property_area', 'area_code', 'rent']
