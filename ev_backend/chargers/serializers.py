from rest_framework import serializers
from .models import EVCharger

class EVChargerSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = EVCharger
        fields = "__all__"
