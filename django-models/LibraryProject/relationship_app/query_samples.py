
from relationship_app.models import Author, Book, Library, Librarian


# Create authors
Haitham = Author.objects.create(name="Haitham")
Mohamed = Author.objects.create(name="Mohamed")

# Create books
book1 = Book.objects.create(title="Book1", author=Haitham)
book2 = Book.objects.create(title="Book2", author=Haitham)
book3 = Book.objects.create(title="Book3", author=Mohamed)

# Create libraries
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

# Add books to libraries (Many-to-Many)
library1.books.add(book1, book2)
library2.books.add(book2, book3)

# Create librarians (One-to-One)
librarian1 = Librarian.objects.create(name="Librarian Haitham", library=library1)
librarian2 = Librarian.objects.create(name="Librarian Mohamed", library=library2)

print("All books in the database:")
for book in Book.objects.all():
    print(book.title)