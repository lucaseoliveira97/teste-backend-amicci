from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from retailer.models import Retailer
from category.models import Category
from .models import Briefing
from .serializers import BriefingSerializer

class BriefingModelSerializer(TestCase):
    def test_serializer_valid_data(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        data = {"id":1,"name":"brif1","retailer":ret,"responsible":"res1","category":cat,"release_date":"date1","availabe":1}
        serializer = BriefingSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_not_valid_data(self):
        data = {'nome':'ret 1'}
        serializer = BriefingSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class briefingAPITest(APITestCase):

    def test_get_briefings(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        Briefing.objects.create(id=1,name="brif1",retailer=ret,responsible="res1",category=cat,release_date="date1",availabe=1)
        url = '/api/demo/briefings/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Briefing.objects.count(), 1)

    def test_get_briefings_empty(self):
        url = '/api/demo/briefings/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_briefing(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        data = {"id":1,"name":"brif1","retailer":"ret1","responsible":"res1","category":"cat1","release_date":"date1","availabe":1}
        url = '/api/demo/briefing/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Briefing.objects.count(), 1)
        self.assertEqual(Briefing.objects.get().name, 'brif1')

    def test_create_briefing_wrong_data(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        data = {"id":1,"namee":"brif1","retailer":"ret1","responsible":"res1","category":"cat1","release_date":"date1","availabe":1}
        url = '/api/demo/briefing/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_briefing_category_does_not_exist(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        data = {"id":1,"namee":"brif1","retailer":"ret1","responsible":"res1","category":"cat2","release_date":"date1","availabe":1}
        url = '/api/demo/briefing/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_briefing_retailer_does_not_exist(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        data = {"id":1,"namee":"brif1","retailer":"ret2","responsible":"res1","category":"cat1","release_date":"date1","availabe":1}
        url = '/api/demo/briefing/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_briefing_not_found(self):
        url = '/api/demo/briefing/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_briefing_found(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        Briefing.objects.create(id=1,name="brif1",retailer=ret,responsible="res1",category=cat,release_date="date1",availabe=1)
        url = '/api/demo/briefing/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Briefing.objects.get().name, 'brif1')

    def test_put_briefing(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        Briefing.objects.create(id=1,name="brif1",retailer=ret,responsible="res1",category=cat,release_date="date1",availabe=1)
        url = '/api/demo/briefing/1'
        data = {"id":1,"name":"brif2","retailer":"ret1","responsible":"res1","category":"cat1","release_date":"date1","availabe":1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Briefing.objects.get().name, 'brif2')

    def test_put_briefing_wrong_data(self):
        cat = Category.objects.create(id=1,name="cat1", description="cat1 desc")
        ret = Retailer.objects.create(id=1,name="ret1")
        Briefing.objects.create(id=1,name="brif1",retailer=ret,responsible="res1",category=cat,release_date="date1",availabe=1)
        url = '/api/demo/briefing/1'
        data = {"id":1,"namee":"brif2","retailer":"ret1","responsible":"res1","category":"cat1","release_date":"date1","availabe":1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

