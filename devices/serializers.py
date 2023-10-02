from rest_framework import serializers
from .models import Device
import re

class DeviceSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    deviceModel = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    note = serializers.CharField(max_length=200)
    serial = serializers.CharField(max_length=200)

    def validate_id(self, value):
        # check if the code matches the required pattern
        pattern = r'(\/devices\/)[\w\d\s]+'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                'This value does not match the required pattern. it should be started with `/devices/`')
        return value
    
    
