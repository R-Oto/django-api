from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
@api_view(['Get','Post'])
def books(request):
    return Response('List of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        return Response({"message":"List of the books"}, status=status.HTTP_200_OK)
    
    def get(self, request):
        return Response({"message":"New Book Created"}, status=status.HTTP_201_CREATED)