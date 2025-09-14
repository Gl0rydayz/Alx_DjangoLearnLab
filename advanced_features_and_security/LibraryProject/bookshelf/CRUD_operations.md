# Complete CRUD Operations - Book Model

This document provides a complete demonstration of Create, Read, Update, and Delete operations using Django's ORM with the Book model.

## Prerequisites
- Django project is set up with the bookshelf app
- Book model is defined and migrated
- Django shell is accessible

## Complete CRUD Workflow

### 1. CREATE Operation
```python
from bookshelf.models import Book

# Create a Book instance with title "1984", author "George Orwell", and publication year 1949
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book}")
```

**Expected Output:**
```
Created: 1984 by George Orwell (1949)
```

### 2. READ Operation
```python
# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

**Expected Output:**
```
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

### 3. UPDATE Operation
```python
# Update the title of "1984" to "Nineteen Eighty-Four" and save the changes
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")
```

**Expected Output:**
```
Updated Title: Nineteen Eighty-Four
```

### 4. DELETE Operation
```python
# Delete the book you created and confirm the deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Number of books remaining: {all_books.count()}")
```

**Expected Output:**
```
Number of books remaining: 0
```

## Complete Shell Session

Here's how the complete session would look in the Django shell:

```python
# Start Django shell: python manage.py shell

# Import the Book model
from bookshelf.models import Book

# CREATE
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book}")

# READ
retrieved_book = Book.objects.get(title="1984")
print(f"Retrieved: {retrieved_book}")
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")

# UPDATE
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated: {retrieved_book}")

# DELETE
retrieved_book.delete()
remaining_books = Book.objects.all()
print(f"Books remaining: {remaining_books.count()}")

# Exit shell
exit()
```

## Expected Complete Output

```
Created: 1984 by George Orwell (1949)
Retrieved: 1984 by George Orwell (1949)
Title: 1984
Author: George Orwell
Publication Year: 1949
Updated: Nineteen Eighty-Four by George Orwell (1949)
Books remaining: 0
```

## Key Django ORM Concepts Demonstrated

1. **Model Creation**: Using `Book.objects.create()` for instant creation and saving
2. **Object Retrieval**: Using `Book.objects.get()` for single object retrieval
3. **Object Updates**: Modifying attributes and calling `save()` method
4. **Object Deletion**: Using `delete()` method to remove objects
5. **QuerySets**: Using `Book.objects.all()` to get all objects
6. **String Representation**: Custom `__str__` method for readable output

## Database Verification

After completing all operations, the database should be empty:
```python
# Verify no books remain
total_books = Book.objects.count()
print(f"Total books in database: {total_books}")
# Output: Total books in database: 0
```

## Notes

- Each operation demonstrates a fundamental CRUD concept
- The operations are designed to be run sequentially
- All operations use Django's built-in ORM methods
- The Book model includes proper string representation for readable output
- Database transactions are automatically handled by Django
