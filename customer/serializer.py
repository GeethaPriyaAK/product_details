from .models import item
from rest_framework import serializers


class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ['id', 'product_name', 'price', 'description']