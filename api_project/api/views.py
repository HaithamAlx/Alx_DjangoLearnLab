from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing CRUD operations on the Book model.
    Provides:
    - list: GET /books_all/
    - retrieve: GET /books_all/<id>/
    - create: POST /books_all/
    - update: PUT /books_all/<id>/
    - partial_update: PATCH /books_all/<id>/
    - destroy: DELETE /books_all/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
