Delete  Book


from bookshelf.models import Book

 Retrieve the book we want to delete (using dynamic ID) In this example i used book.id  i also could use id =  1 
book_to_delete = Book.objects.get(id=book.id)


book_to_delete.delete()

Verify deletion by retrieving all books

all_books = Book.objects.all()
print(all_books)


expected output will look like the following 

(1, {'bookshelf.Book': 1})  # indicates 1 object deleted
<QuerySet []>               # confirms that no books exist in the database
