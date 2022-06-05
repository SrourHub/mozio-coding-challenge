from .models import Provider, ServiceArea
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import ProviderSerializer, ServiceAreaSerializer


# Create your tests here.

class ProviderTestCase(APITestCase):

    def test_post_provider(self):

        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
                    "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        response = self.client.post("/providers/", data)

        response_data = response.json()

        del response_data['id']

        self.assertEqual(response_data, data)

    def test_get_providers(self):

        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
                    "phone_number": "76846119", "language": "english", "currency": "USD"}
        data2 = {"name": "Mozio", "email": "mozio@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        serializer = ProviderSerializer(data = data)
        serializer2 = ProviderSerializer(data = data2)
        
        if serializer.is_valid():
            serializer.save()
        if serializer2.is_valid():
            serializer2.save()

        response = self.client.get("/providers/")
        self.assertEqual(len(response.json()), 2)

    def test_get_one_provider(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        response = self.client.get("/providers/1")
        response_data = response.json()

        del response_data['id']

        self.assertEqual(response_data, data)

    def test_update_provider(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        data = {"name": "Ali Srour", "email": "srourali07@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}

        response = self.client.put("/providers/1", data)

        response_data = response.json()

        del response_data['id']

        self.assertEqual(response_data, data)

    def test_delete_provider(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        response = self.client.delete("/providers/1")

        providers = Provider.objects.all()

        self.assertEqual(len(providers), 0)
        

class ServiceAreaTestCase(APITestCase):

    def test_post_service_area(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        
        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}
        
        response = self.client.post("/service_areas/", data,format="json")
        response_data = response.json()

        del response_data['id']
        del response_data['provider_name']

        self.assertEqual(response_data, data)

    def test_get_service_areas(self):

        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        
        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}
        data2 = {"name": "Las Vegas", "price": 180.2, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}
        serializer = ServiceAreaSerializer(data = data)
        serializer2 = ServiceAreaSerializer(data = data2)
        
        if serializer.is_valid():
            serializer.save()
        if serializer2.is_valid():
            serializer2.save()

        response = self.client.get("/service_areas/")
        self.assertEqual(len(response.json()), 2)

    def test_get_one_service_area(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        
        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}

        serializer = ServiceAreaSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()

        response = self.client.get("/service_areas/1")
        response_data = response.json()

        del response_data['id']
        del response_data['provider_name']

        self.assertEqual(response_data, data)

    def test_update_service_area(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}

        serializer = ServiceAreaSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
        
        data = {"name": "some name edited", "price": 170.5, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}

        response = self.client.put("/service_areas/1", data, format='json')

        response_data = response.json()

        del response_data['id']
        del response_data['provider_name']

        self.assertEqual(response_data, data)

    def test_delete_service_area(self):
        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}

        serializer = ServiceAreaSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()

        response = self.client.delete("/service_areas/1")

        service_areas = ServiceArea.objects.all()

        self.assertEqual(len(service_areas), 0)

    def test_polygons_that_contain_point(self):

        data = {"name": "Ali Sroiur", "email": "srour@gmail.com", 
            "phone_number": "76846119", "language": "english", "currency": "USD"}
        
        serializer = ProviderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        data = {"name": "California", "price": 260.67, "geojson_information":{
            "type": "Polygon", 
            "coordinates": [
                [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
            ]
        }, "provider": 1}

        serializer = ServiceAreaSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()

        response = self.client.get("/service_areas/contain_point/20.1/20.2")
        self.assertEqual(len(response.json()), 1)


        

