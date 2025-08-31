# Create Operation - Book Model

## Command Used
```python
from bookshelf.models import Book

# Create a Book instance with title "1984", author "George Orwell", and publication year 1949
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```
<Book: 1984 by George Orwell (1949)>
```

## What Happens
- A new Book instance is created in the database
- The `__str__` method returns a formatted string representation
- The book is automatically saved to the database
- A unique ID is automatically assigned to the book

## Alternative Method
```python
# Alternative way to create and save a book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```
