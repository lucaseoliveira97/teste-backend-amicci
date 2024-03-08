from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

class CategoryModelSerializer(TestCase):
    def test_serializer_valid_data(self):
        data = {'name':'Categoria 1', 'description':'Categoria 1 descricao'}
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_not_valid_data(self):
        data = {'nome':'Categoria 1', 'description':'Categoria 1 descricao'}
        serializer = CategorySerializer(data=data)
        self.assertFalse(serializer.is_valid())

class CategoryAPITest(APITestCase):

    def test_get_categories(self):
        Category.objects.create(name="cat1", description="cat1 desc")
        url = '/api/demo/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_categories_empty(self):
        url = '/api/demo/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {'name': 'cat2', "description":"cat2 desc"}
        url = '/api/demo/category/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'cat2')
    
    def test_get_category_not_found(self):
        url = '/api/demo/category/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_category_found(self):
        Category.objects.create(id=1,name="cat1", description="cat1 desc")
        url = '/api/demo/category/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'cat1')

    def test_put_category(self):
        Category.objects.create(id=1,name="cat1", description="cat1 desc")
        url = '/api/demo/category/1'
        data = {'name': 'cat2', "description":"cat2 desc"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'cat2')