from rest_framework import serializers

from app_market.models import Good


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'
