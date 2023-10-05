from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from devices.serializers import DeviceSerializer
from .models import Device


class DeviceListApiView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Creates the Device with given device data
        """
        data = {
            'id': request.data['id'],
            'deviceModel': request.data['deviceModel'],
            'name': request.data['name'],
            'note': request.data['note'],
            'serial': request.data['serial'],
        }
        serializer = DeviceSerializer(data=data)  # type: ignore

        serializer.is_valid(raise_exception=True)
        device = Device(serializer.data['id'],
                        deviceModel=serializer.data['deviceModel'],
                        name=serializer.data['name'],
                        note=serializer.data['note'],
                        serial=serializer.data['serial'])
        try:
            device.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except :
            return Response({'message': 'Cannot create device'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeviceDetailApiView(APIView):
    def get_object(self, device_id):
        """
        Helper method to get the object with given device_id
        """
        id_prefix = '/devices/'
        try:
            return Device.get(id_prefix + device_id)
        except Device.DoesNotExist: # type: ignore
            return None

    def get(self, request, device_id, *args, **kwargs):
        """
        Retrieves the Device with given device_id
        """
        device = self.get_object(device_id)

        if not device:
            return Response(
                {'message': 'Device with given id does not exists.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)
