from django.shortcuts import render
from . models import Book, BookInstance, Author, Genre


# Create your views here.
def index(request):

    # Generate number of books available
    num_books = Book.objects.all().count()
    # Generate number of instances of books
    num_instances = BookInstance.objects.all().count()

    # Available copies (status='a')
    instances_available = BookInstance.objects.filter(status_exact='a').count()

    # Count the number of authors
    num_authors = Author.objects.all()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)