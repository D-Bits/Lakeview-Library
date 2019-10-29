from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Book, BookInstance, Author, Genre


# Create your views here.
def index(request):

    # Generate number of books available
    num_books = Book.objects.all().count()
    # Generate number of instances of books
    num_instances = BookInstance.objects.all().count()

    # Available copies (status='a')
    instances_available = BookInstance.objects.filter(status='a').count()

    # Count the number of authors
    num_authors = Author.objects.all()

    # Count the no. of visits to this view in a session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


# View to show all books
class BookListView(ListView):

    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'catalog/book_list.html'
    paginate_by = 10 


# For details of individual books
class BookDetailView(DetailView):

    model = Book