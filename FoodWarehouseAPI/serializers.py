from dataclasses import field
from rest_framework import serializers
from . models import Foods

class FoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foods
        fields = ('Mfd_id', 'Name', 'UnitPrice', 'UnitsInStock')