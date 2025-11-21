from django.db import models
from rest_framework import serializers
from .models import Book

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
