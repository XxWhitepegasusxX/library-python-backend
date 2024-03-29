from rest_framework import serializers
from .models import Author, Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')