from rest_framework import serializers
from .models import MQTTData

class MQTTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MQTTData
        fields = '__all__'