from bookshelf.models import Book

Retrieve the book we want to update (using dynamic ID)
book_to_update = Book.objects.get(id=book.id)

Update the title of the book
book_to_update.title = "Nineteen Eighty-Four"

Save the changes
book_to_update.save()

 Verify the update by retrieving the book again
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)


expected output 

Nineteen Eighty-Four

