from django.shortcuts import render
from .models import item
from .serializer import itemserializer
from rest_framework .decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def item_list(request):
    if request.method == 'GET':
        product = item.objects.all()
        serializer = itemserializer(product, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = itemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])

def item_detail(request,pk):
  try:
      products = item.objects.get(pk=pk) 
  except item.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
  if request.method == 'GET':
    serializer = itemserializer(products)
    return Response(serializer.data)
  
  elif request.method =='PUT':
      serializer = itemserializer(products,data=request.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
      products.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
      
        

