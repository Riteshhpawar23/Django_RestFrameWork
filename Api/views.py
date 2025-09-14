from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    """
    A simple API endpoint that returns a hello world message
    """
    return Response({
        'message': 'Hello World! Your Rest_main API is working!',
        'status': 'success'
    })