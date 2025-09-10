from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def studentview(request):
    return JsonResponse({'name':'Ravi','age':24})
