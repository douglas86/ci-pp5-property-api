from rest_framework import serializers

from .models import Stocks


class StockSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='owner.username')
    property_image = serializers.ReadOnlyField()
    property_address = serializers.SerializerMethodField()
    property_area = serializers.SerializerMethodField()
    area_code = serializers.SerializerMethodField()
    rent = serializers.IntegerField()

    size = 1024 * 1024 * 2
    width = 4096
    height = 4096

    def validate_image(self, value):
        if value.size > self.size:
            raise serializers.ValidationError('Image size larger than 2MB')
        if value.image.width > self.width:
            raise serializers.ValidationError('Image width larger than 4096')
        if value.image.height > self.height:
            raise serializers.ValidationError('Image height larger than 4096')
        return value

    class Meta:
        model = Stocks
        fields = ['id', 'product', 'property_image', 'property_address', 'property_area', 'area_code', 'rent']
        read_only_fields = ['product', 'property_image']

    def get_property_address(self, obj):
        return obj.property_address

    def get_property_area(self, obj):
        return obj.property_area

    def get_area_code(self, obj):
        return obj.area_code

    def create(self, validated_data):
        owner = self.context['request'].user
        validated_data.pop('owner', None)
        property_address = self.context['request'].data.get('property_address', 'Default address')
        property_area = self.context['request'].data.get('property_area', 'Default area')
        area_code = self.context['request'].data.get('area_code', 'Default area')

        stocks_instance = Stocks.objects.create(
            owner=owner,
            property_address=property_address,
            property_area=property_area,
            area_code=area_code,
            **validated_data
        )

        return stocks_instance
