from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
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