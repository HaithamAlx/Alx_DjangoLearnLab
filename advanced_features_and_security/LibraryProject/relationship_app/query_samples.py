from relationship_app.models import Author, Book, Library, Librarian



Haitham = Author.objects.get_or_create(name="Haitham")[0]
Mohamed = Author.objects.get_or_create(name="Mohamed")[0]

book1 = Book.objects.get_or_create(title="Book1", author=Haitham)[0]
book2 = Book.objects.get_or_create(title="Book2", author=Haitham)[0]
book3 = Book.objects.get_or_create(title="Book3", author=Mohamed)[0]

library1 = Library.objects.get_or_create(name="Central Library")[0]
library2 = Library.objects.get_or_create(name="Community Library")[0]

library1.books.add(book1, book2)
library2.books.add(book2, book3)

librarian1 = Librarian.objects.get_or_create(name="Librarian Haitham", library=library1)[0]
librarian2 = Librarian.objects.get_or_create(name="Librarian Mohamed", library=library2)[0]


library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print(f"Books in {library_name}:")
for book in books_in_library:
    print(book.title)


author_name = "Haitham"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"\nBooks by {author_name}:")
for book in books_by_author:
    print(book.title)


librarian = library.librarian
print(f"\nLibrarian of {library_name}: {librarian.name}")

librarian_from_model = Librarian.objects.get(library=library)
print(f"Librarian of {library_name} (via Librarian model): {librarian_from_model.name}")