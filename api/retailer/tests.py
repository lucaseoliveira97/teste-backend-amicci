from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Retailer
from .serializers import RetailerSerializer

class RetailerModelSerializer(TestCase):
    def test_serializer_valid_data(self):
        data = {'name':'Vendor 1'}
        serializer = RetailerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_not_valid_data(self):
        data = {'nome':'Vendor 1'}
        serializer = RetailerSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class RetailerAPITest(APITestCase):

    def test_get_retailers(self):
        Retailer.objects.create(name="ret1")
        url = '/api/demo/retailers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retailers_empty(self):
        url = '/api/demo/retailers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_retailer(self):
        data = {'name': 'ret2'}
        url = '/api/demo/retailer/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Retailer.objects.count(), 1)
        self.assertEqual(Retailer.objects.get().name, 'ret2')
    
    def test_get_retailer_not_found(self):
        url = '/api/demo/retailer/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_retailer_found(self):
        Retailer.objects.create(id=1,name="ret1")
        url = '/api/demo/retailer/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Retailer.objects.get().name, 'ret1')

    def test_put_retailer(self):
        Retailer.objects.create(id=1,name="ret1")
        url = '/api/demo/retailer/1'
        data = {'name': 'ret2'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Retailer.objects.get().name, 'ret2')