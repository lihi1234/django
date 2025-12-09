from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(req):
    return JsonResponse('index', safe=False)

def hello(req):
    return JsonResponse('hello', safe=False)




@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
def test(req):
    return Response({'username':'blabla'})

# Create your views here.
