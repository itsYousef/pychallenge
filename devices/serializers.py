from rest_framework import serializers
from .models import Device
import re

class DeviceSerializer(serializers.ModelSerializer):
    # id = serializers.RegexField(r'(\/devices\/)[\w\d\s]+')
    
    def validate_id(self, value):
        # check if the code matches the required pattern
        pattern = r'(\/devices\/)[\w\d\s]+'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                'This value does not match the required pattern. it should be started with `/devices/`')
        return value
    
    class Meta:
        model = Device
        fields = ["id", "device_model", "name", "note", "serial"]
