from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET','POST'])
def Item_list(request):
     
     if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data) 
     if request.method == "POST":
         serializer = ItemSerializer(data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         
@api_view(['GET','PUT','DELETE'])
def Item_detail(request, id):
    
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


