from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from .serializers import DeviceSerializer


class DeviceListApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create the Device with given device data
        '''
        data = {
            'id': request.data.get('id'),
            'device_model': request.data.get('deviceModel'),
            'name': request.data.get('name'),
            'note': request.data.get('note'),
            'serial': request.data.get('serial'),
        }
        serializer = DeviceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetailApiView(APIView):
    def get_object(self, device_id):
        '''
        Helper method to get the object with given device_id
        '''
        id_prefix = '/devices/'
        try:
            return Device.objects.get(id=id_prefix + device_id)
        except Device.DoesNotExist:
            return None

    def get(self, request, device_id, *args, **kwargs):
        '''
        Retrieves the Device with given device_id
        '''
        founded_device = self.get_object(device_id)
        if not founded_device:
            return Response(
                {"res": "Device with given id does not exists."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DeviceSerializer(founded_device)
        return Response(serializer.data, status=status.HTTP_200_OK)
