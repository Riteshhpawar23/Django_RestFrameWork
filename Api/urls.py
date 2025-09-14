
from django.urls import path
from . import views

urlpatterns = [
    # Test endpoint
    path('hello/', views.hello_world, name='hello-world'),
    # Add your API endpoints here
]
