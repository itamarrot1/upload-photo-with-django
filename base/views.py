from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.serializer import CarSerializer
from .models import Car

@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
def get_cars(req):
    return Response(CarSerializer(Car.objects.all(), many=True).data)