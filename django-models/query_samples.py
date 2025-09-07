# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

# Import models AFTER setting up Django
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # === Create Sample Data ===
    # Using get_or_create to avoid creating duplicates on subsequent runs
    author1, _ = Author.objects.get_or_create(name='J.R.R. Tolkien')
    book1, _ = Book.objects.get_or_create(title='The Hobbit', author=author1)
    book2, _ = Book.objects.get_or_create(title='The Lord of the Rings', author=author1)

    library1, _ = Library.objects.get_or_create(name='Central City Library')
    librarian1, _ = Librarian.objects.get_or_create(name='Eleanor Vance', library=library1)
    
    # Add books to the library's many-to-many field
    library1.books.add(book1, book2)

    print("--- Sample Data Created ---\n")

    # === Perform Queries ===

    # 1. Query all books by a specific author
    print(f"1. Querying all books by '{author1.name}':")
    # We use the reverse relationship manager 'book_set'
    tolkien_books = author1.book_set.all()
    for book in tolkien_books:
        print(f"   - {book.title}")
    print("-" * 20)

    # 2. List all books in a library
    print(f"2. Listing all books in '{library1.name}':")
    # We access the many-to-many field directly
    library_books = library1.books.all()
    for book in library_books:
        print(f"   - {book.title}")
    print("-" * 20)

    # 3. Retrieve the librarian for a library
    print(f"3. Retrieving the librarian for '{library1.name}':")
    # We use the reverse one-to-one relationship
    the_librarian = library1.librarian
    print(f"   - The librarian is {the_librarian.name}")
    print("-" * 20)


if __name__ == '__main__':
    run_queries()