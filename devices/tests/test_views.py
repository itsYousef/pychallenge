from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from devices.models import Device


class DeviceTests(APITestCase):
    def test_create_device(self):
        """
        Ensure we can create a new device object.
        """
        url = reverse('device_list')
        data = {
            'id': '/devices/id7',
            'deviceModel': '/devicemodels/id1',
            'name': 'Sensor',
            'note': 'Testing a sensor.',
            'serial': 'A020000102'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.get().name, 'Sensor')

    def test_get_one_device(self):
        """
        Ensure that we can get a single device
        """
        data = {
            'id': '/devices/id7',
            'device_model': '/devicemodels/id1',
            'name': 'Sensor',
            'note': 'Testing a sensor.',
            'serial': 'A020000102'
        }

        Device.objects.create(id=data.get('id'),
                              device_model=data.get('device_model'),
                              name=data.get('name'),
                              note=data.get('note'),
                              serial=data.get('serial'))

        url = reverse('device_detail', args=['id7'])
        response = self.client.get(url)

        self.assertEqual(response.data.get('id'), data.get('id'))
