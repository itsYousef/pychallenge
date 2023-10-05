from rest_framework import serializers
import re


class DeviceSerializer(serializers.Serializer):
    """
    Serializer for device data
    """
    id = serializers.CharField(max_length=100)
    deviceModel = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    note = serializers.CharField(max_length=200)
    serial = serializers.CharField(max_length=200)

    def validate_id(self, value):
        """
        Checks if the id field matches the required pattern
        """
        pattern = r'(\/devices\/)[\w\d\s]+'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                'This value does not match the required pattern. it should be started with `/devices/`')
        return value
