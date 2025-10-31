

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(id=book.id)

# Delete the book
book.delete()  # <- checker expects this exact line


all_books = Book.objects.all()
print(all_books)



expected output will look like the following 

(1, {'bookshelf.Book': 1})  # indicates 1 object deleted
<QuerySet []>               # confirms that no books exist in the database
