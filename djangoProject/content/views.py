from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContentSerializer, CategorySerializer, EventSerializer
from .models import *

class list_content(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        return Content.objects.order_by('-posted',).all()

class list_category(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Content.objects.order_by('slug',).all()

class list_event(generics.ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        return "html"



