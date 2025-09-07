# relationship_app/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # A ForeignKey creates a many-to-one relationship.
    # Many books can belong to one author.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    # A ManyToManyField creates a many-to-many relationship.
    # A library can have many books, and a book can be in many libraries.
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # A OneToOneField creates a strict one-to-one relationship.
    # One librarian is assigned to exactly one library.
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name