from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string_response(request):
    return HttpResponse('This is my frist string')


def second_string(request):
    return HttpResponse('This is my second string')

def third_string(request):
    return HttpResponse('This is my third String')
    
