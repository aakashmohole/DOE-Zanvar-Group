from rest_framework import serializers
from .models import DoeData

class DoeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoeData
        fields = '__all__'  # Serialize all fields
