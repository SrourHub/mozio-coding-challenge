from django.shortcuts import render
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shapely.geometry import Point, Polygon

@api_view(['GET', 'POST'])
def provider_list(request, format=None):
    """
    If the request is a GET, return a list of all providers. 
    If the request is a POST, create a new provider

    For Post request it requires a body:
    Example:
        {
            "name": "name",
            "email": "email@gmail.com",
            "phone_number": "12345678",
            "language": "english",
            "currency": "USD"
        }
    """
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProviderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def provider_details(request, id,format=None):
    """
    If the request is a GET, return the provider with the given id. 

    If the request is a PUT, update the details of the provider with the given input data
    For PUT request it requires a body:
    Example:
        {
            "name": "name",
            "email": "email@gmail.com",
            "phone_number": "12345678",
            "language": "english",
            "currency": "USD"
        }

    If the request is a DELETE, delete the provider from the database

    """
    try:
        provider = Provider.objects.get(pk=id)
    except Provider.DoesNotExist:
        return Response(status= status.HTTP_200_OK)

    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider.delete()
        return Response(id, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def service_area_list(request,format=None):
    """
    If the request is a GET, return all the service areas. 
    If the request is a POST, create a new service area.
    For Post request it requires a body:
    Example:
        {
            "name": "example",
            "price": 125.69,
            "geojson_information":{
                    "type": "Polygon", 
                    "coordinates": [
                        [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
                    ]
                },
            "provider": 1
        }
    """

    if request.method == 'GET':
        service_areas = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_areas, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServiceAreaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def service_area_details(request, id,format=None):
    """
    If the request is a GET, return the service area with the given id. 

    If the request is a PUT, update the details of the service area with the given input data
    For PUT request it requires a body:
    Example:
        {
            "name": "example",
            "price": 125.69,
            "geojson_information":{
                    "type": "Polygon", 
                    "coordinates": [
                        [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]
                    ]
                },
            "provider": 1
        }

    If the request is a DELETE, delete the service area from the database
    """
    try:
        service_area = ServiceArea.objects.get(pk=id)
    except ServiceArea.DoesNotExist:
        return Response(status = status.HTTP_200_OK)

    if request.method == 'GET':
        serializer = ServiceAreaSerializer(service_area)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ServiceAreaSerializer(service_area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        service_area.delete()
        return Response(id, status = status.HTTP_200_OK)

@api_view(['GET'])
def service_areas_that_contain_given_lat_lng(request,lat,lng,format=None):
    """
    It takes a lat and lng as input, and returns a list of service areas that contain that point
    If there aren't any, it returns an empty list
    """
    point = Point(float(lat),float(lng))
    service_areas = ServiceArea.objects.all()
    serializer = ServiceAreaSerializer(service_areas, many = True)

    service_areas_that_contain_point = []
    for service_area in serializer.data:
        service_area = dict(service_area)
        coordinates = service_area['geojson_information']['coordinates']
        polygon = Polygon([tuple(x) for x in coordinates])
        if point.within(polygon):
            service_areas_that_contain_point.append({'polygon_name': service_area['name'],'provider_name':service_area['provider_name'],'price':service_area['price']})

    return Response(service_areas_that_contain_point, status=status.HTTP_200_OK)








