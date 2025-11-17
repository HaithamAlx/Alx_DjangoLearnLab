from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Book
from .forms import BookForm


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/edit_book.html', {'form': form})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/create_book.html', {'form': form})


def search_books(request):
    query = request.GET.get('q', '').strip()

    # Limit query length to avoid abuse
    if len(query) > 100:
        query = query[:100]

    results = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query)
    ) if query else []

    return render(request, 'bookshelf/search_results.html', {
        'query': query,
        'results': results,
    })
