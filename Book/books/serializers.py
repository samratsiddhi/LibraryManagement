from rest_framework import serializers
from .models import Category,Books

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ['name',]
    
class BookSerializer(serializers.ModelSerializer):
    model = Books
    fields = ['name','quantity','category']