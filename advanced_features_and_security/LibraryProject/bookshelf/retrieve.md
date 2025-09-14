# Retrieve Operation - Book Model

## Command Used
```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

## Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

## Alternative Retrieval Methods

### Get All Books
```python
# Retrieve all books in the database
all_books = Book.objects.all()
for book in all_books:
    print(book)
```

### Filter Books
```python
# Filter books by author
orwell_books = Book.objects.filter(author="George Orwell")

# Filter books by publication year
books_1949 = Book.objects.filter(publication_year=1949)
```

### Get First/Last
```python
# Get the first book
first_book = Book.objects.first()

# Get the last book
last_book = Book.objects.last()
```

## What Happens
- The `get()` method retrieves a single object that matches the criteria
- If multiple objects match, it raises an error
- If no objects match, it raises a `DoesNotExist` exception
- The `filter()` method returns a QuerySet of all matching objects
