from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Books
from .serializers import BookSerializer,CategorySerializer, BorrowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
class BorrowView(APIView):
    def get(self,request):
        serializer = BorrowSerializer()
        books = serializer.get_books()
        return Response(books)
    
    def post(self,request):
        return Response("hello")
    
    

