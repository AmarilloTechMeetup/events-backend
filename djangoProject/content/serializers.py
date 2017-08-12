from rest_framework import serializers
from .models import *

class ContentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    category = serializers.StringRelatedField()
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Content
        fields = ('title', 'slug', 'body', 'posted', 'category')

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
         
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = '__all__'
