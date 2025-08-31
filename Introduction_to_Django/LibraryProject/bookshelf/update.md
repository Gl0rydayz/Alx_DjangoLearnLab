# Update Operation - Book Model

## Command Used
```python
from bookshelf.models import Book

# Update the title of "1984" to "Nineteen Eighty-Four" and save the changes
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

## Expected Output
```python
# After updating, retrieve the book to confirm changes
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")
print(f"Author: {updated_book.author}")
print(f"Publication Year: {updated_book.publication_year}")
```

## Console Output
```
Updated Title: Nineteen Eighty-Four
Author: George Orwell
Publication Year: 1949
```

## Alternative Update Methods

### Update Multiple Fields
```python
# Update multiple fields at once
book.title = "Nineteen Eighty-Four"
book.publication_year = 1950
book.save()
```

### Bulk Update
```python
# Update multiple books at once
Book.objects.filter(author="George Orwell").update(publication_year=1950)
```

### Using update() Method
```python
# Update without retrieving the object first
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
```

## What Happens
- The `save()` method persists the changes to the database
- Only the modified fields are updated in the database
- The object's attributes are updated in memory
- The database transaction is committed
