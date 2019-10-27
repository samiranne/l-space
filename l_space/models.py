from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)

    def __str__(self):
        return f"Book '{self.title}'"


class OwnedBook(models.Model):
    book_id = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
