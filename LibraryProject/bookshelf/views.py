from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm

def book_search(request):
    query = request.GET.get('q', '')
    if query:
        # Use ORM to prevent SQL injection
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe handling of user input
            return render(request, 'bookshelf/success.html')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")