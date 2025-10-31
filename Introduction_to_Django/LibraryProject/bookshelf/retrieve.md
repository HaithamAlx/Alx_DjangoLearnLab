from bookshelf.models import Book


retrieved_book = Book.objects.get(id=1)
OR


retrieved_book = Book.objects.get(id=book.id)

# Display all attributes
print("Title:", retrieved_book.title)
print("Author:", retrieved_book.author)
print("Publication Year:", retrieved_book.publication_year)
retrieved_book



id = 1
1 is the first object i created out of this class in our example
that object contains all the definied attributes "title, author and publication year)

django when it pulls the data out the data base, it use ID 




expected output


>>> print("Title:", retrieved_book.title)
Title: 1984
>>> print("Author:", retrieved_book.author)
Author: George Orwell
>>> print("Publication Year:", retrieved_book.publication_year)
Publication Year: 1949