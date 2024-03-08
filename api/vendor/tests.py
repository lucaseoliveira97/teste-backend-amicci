from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer

class VendorModelSerializer(TestCase):
    def test_serializer_valid_data(self):
        data = {'name':'Vendor 1'}
        serializer = VendorSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_not_valid_data(self):
        data = {'nome':'Vendor 1'}
        serializer = VendorSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class VendorAPITest(APITestCase):

    def test_get_vendors(self):
        Vendor.objects.create(name="ret1")
        url = '/api/demo/vendors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_vendors_empty(self):
        url = '/api/demo/vendors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vendor(self):
        data = {'name': 'ret2'}
        url = '/api/demo/vendor/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)
        self.assertEqual(Vendor.objects.get().name, 'ret2')
    
    def test_get_vendor_not_found(self):
        url = '/api/demo/vendor/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_vendor_found(self):
        Vendor.objects.create(id=1,name="ret1")
        url = '/api/demo/vendor/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get().name, 'ret1')

    def test_put_vendor(self):
        Vendor.objects.create(id=1,name="ret1")
        url = '/api/demo/vendor/1'
        data = {'name': 'ret2'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get().name, 'ret2')