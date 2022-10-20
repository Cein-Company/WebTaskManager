from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from loginapi.models import Loginapi
from loginapi.serializers import LoginapiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
def loginapi_list(request):
    if request.method == 'GET':
        loginapis = Loginapi.objects.all()
        serializer = LoginapiSerializer(loginapis, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoginapiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def loginapi_detail(request, pk):
    try:
        snippet = Loginapi.objects.get(pk=pk)
    except Loginapi.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LoginapiSerializer(snippet)
        return JsonResponse(serializer.data)

@api_view(['GET', 'POST'])
def loginapi_list(request, format=None):
    """
    List all login attempts, or create a new one.
    """
    if request.method == 'GET':
        loginapis = Loginapi.objects.all()
        serializer = LoginapiSerializer(loginapis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoginapiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def loginapi_detail(request, pk, format=None):
    try:
        snippet = Loginapi.objects.get(pk=pk)
    except Loginapi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoginapiSerializer(snippet)
        return Response(serializer.data)