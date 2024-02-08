from rest_framework import serializers
from .models import Category,Books

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'