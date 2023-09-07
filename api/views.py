from rest_framework import generics
from .models import Book, Category, Author
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        book = self.request.query_params.get('id')
        if book is not None:
            queryset = queryset.filter(Book=book)
        return queryset
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        author = self.request.query_params.get('id')
        if author is not None:
            queryset = queryset.filter(Author=author)
        return queryset
    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        category = self.request.query_params.get('id')
        if category is not None:
            queryset = queryset.filter(Category=category)
        return queryset
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()