from django import forms
from rest_framework import serializers
from meb.models import Product,ProductImg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'








