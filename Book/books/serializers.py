from rest_framework import serializers
from .models import Category,Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','name','quantity',]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class BorrowSerializer(serializers.Serializer):
    books = serializers.SerializerMethodField()
    
    def get_books(self):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return serializer.data
 
    # def validate(self, attrs):
    #     return super().validate(attrs)
    