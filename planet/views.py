from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Inner
from .serializer import InnerSerializer
# Create your views here.
# localhost:3000/Inners/ get post
# localhost:3000/Inners/:id  get delete update
class InnersView(APIView):
    """View calls for Inners/ for viewing all and creating"""
    def get(self, request):
        inners = Inner.objects.all()
        serializer = InnerSerializer(inners, many=True) 
        return Response({'inners': serializer.data})
    def post(self, request):
        serializer = InnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InnersDetailViews(APIView):
    """View class for inners/:pk for viewing updating and deleting"""
    def get(self, request, pk):
        inner = get_object_or_404(Inner, pk=pk)
        serializer = InnerSerializer(inner)
        return Response({'inner': serializer.data})
    def patch(self, request, pk):
        inner = get_object_or_404(inner, pk=pk)
        serializer = InnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        inner = get_object_or_404(Inner, pk=pk)
        inner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 