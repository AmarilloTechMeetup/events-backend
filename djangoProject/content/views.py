from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContentSerializer, CategorySerializer
from .models import *

class list_content(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        return Content.objects.order_by('-posted',).all()

class list_category(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Content.objects.order_by('slug',).all()

class content_by_param(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        # slug = self.kwargs['slug']
        slug = self.request.GET.get('slug')
        if slug:
            return Content.objects.filter(slug=slug)

        id = self.request.GET.get('category') 
        category = Category.objects.filter(slug=id)
        purpose = self.request.GET.get('purpose')
        if purpose and category:
            return Content.objects.order_by('-posted',).filter(purpose=purpose, category=category)
        if purpose:
            return Content.objects.order_by('-posted',).filter(purpose=purpose)
        if category:
            return Content.objects.order_by('-posted',).filter(category=category)
         
        return Content.objects.order_by('-posted',).all()


