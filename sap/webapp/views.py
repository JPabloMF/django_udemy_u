from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse('Hello world!')

def bye(request):
    return HttpResponse('Bye world!')

def contact(request):
    return HttpResponse('Tel: 111111, name: Sandro')