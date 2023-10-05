import os
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APISimpleTestCase
from devices.models import Device
import boto3

DB_TABLE = os.getenv('DB_TABLE')


class DeviceTests(APISimpleTestCase):
    @classmethod
    def setUpClass(cls):
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.getenv('DYNAMODB_LOCAL_ENDPOINT'))

        try:
            table = dynamodb.create_table(  # type: ignore
                TableName=DB_TABLE,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 2
                }
            )
            table.wait_until_exists()
        except:
            print('Cannot create table.')

    @classmethod
    def tearDownClass(cls):
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.getenv('DYNAMODB_LOCAL_ENDPOINT'))
        try:
            table = dynamodb.Table(DB_TABLE)  # type: ignore
            table.delete()
        except:
            print('Table does not exists!')

    def test_create_device(self):
        """
        Test creating a new device object.
        """
        url = reverse('device_list')
        data = {
            'id': '/devices/id1',
            'deviceModel': '/devicemodels/id1',
            'name': 'Sensor',
            'note': 'Testing a sensor.',
            'serial': 'A020000102'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.count(data['id']), 1)
        self.assertEqual(Device.get(data['id']).name, 'Sensor')
        
    def test_create_device_fail(self):
        """
        Test getting Bad Request error when any of payload fields missing.
        """
        url = reverse('device_list')
        data = {
            'id': '/devices/id2',
            # 'deviceModel': '/devicemodels/id2',
            'name': 'Sensor',
            'note': 'Testing a sensor.',
            'serial': 'A020000102'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_get_one_device(self):
        """
        Test getting a single device detail.
        """
        data = {
            'id': '/devices/id3',
            'deviceModel': '/devicemodels/id3',
            'name': 'Sensor',
            'note': 'Testing a sensor.',
            'serial': 'A020000102'
        }

        device = Device(id=data['id'],
                        deviceModel=data['deviceModel'],
                        name=data['name'],
                        note=data['note'],
                        serial=data['serial'])
        device.save()

        url = reverse('device_detail', args=[data['id'].split('/')[-1]])
        response = self.client.get(url)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], data['id'])  # type: ignore
        
    def test_get_one_device_fail(self):
        """
        Test getting Not Found error when device with requested id does not exists.
        """
        url = reverse('device_detail', args=['id8'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
