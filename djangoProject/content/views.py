from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContentSerializer, CategorySerializer, EventSerializer
from .models import *
from django.views.decorators.csrf import csrf_exempt

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
        return Event.objects.all()

@api_view(['GET', 'POST'])
def list_event(request):
    """
    List all snippets, or create a new snippet.
    """
    
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
