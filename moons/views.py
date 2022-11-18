from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Outer
from .serializer import OuterSerializer
# Create your views here.
# localhost:3000/Outers/ get post
# localhost:3000/Outers/:id  get delete update
class OutersView(APIView):
    """View calls for Outers/ for viewing all and creating"""
    def get(self, request):
        outers = Outer.objects.all()
        serializer = OuterSerializer(outers, many=True) 
        return Response({'outers': serializer.data})
    def post(self, request):
        serializer = OuterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OutersDetailViews(APIView):
    """View class for outers/:pk for viewing updating and deleting"""
    def get(self, request, pk):
        outer = get_object_or_404(Outer, pk=pk)
        serializer = OuterSerializer(outer)
        return Response({'outer': serializer.data})
    def patch(self, request, pk):
        outer = get_object_or_404(outer, pk=pk)
        serializer = OuterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        outer = get_object_or_404(Outer, pk=pk)
        outer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 