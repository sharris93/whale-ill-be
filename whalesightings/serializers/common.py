from rest_framework import serializers
from ..models import WhaleSighting

class WhaleSightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhaleSighting
        fields = '__all__'