from django.shortcuts import render
from rest_framework import viewsets
from . serializers import FoodsSerializer
from . models import Foods

# Create your views here.

class Foodsviewset(viewsets.ModelViewSet):
    queryset = Foods.objects.all().order_by('Mfd_id')
    serializer_class = FoodsSerializer