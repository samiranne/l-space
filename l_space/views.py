from django.views import generic

from .models import Book


class BooksView(generic.ListView):
    model = Book
    template_name = "l_space/books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.order_by("title")
