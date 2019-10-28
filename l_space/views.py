from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("title")
    serializer_class = BookSerializer
