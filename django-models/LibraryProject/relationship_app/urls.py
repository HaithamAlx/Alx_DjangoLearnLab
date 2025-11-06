from django.urls import path
from .views import list_books, library_detail

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:library_id>/', library_detail, name='library_detail'),
]


