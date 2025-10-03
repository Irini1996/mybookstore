from django.shortcuts import render #Import the render function.
#render() is used to take a request, a template, and some context (data), and then return an HTML response.
from django.db.models import Q #Q allows you to create complex database queries using logical operators like OR and AND.
from .models import Book

def book_list(request): #Define a view function called book_list
    query = request.GET.get('q', '')  #Check the query parameters in the URL.
#If the user visited /books/?q=tolstoy, then query will be "tolstoy".
#If there is no q parameter, it defaults to an empty string

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
        #If the user typed something in the search bar:
        #Filter books where the title or the author contains the query (case-insensitive).
        #Example: searching for "tolstoy" will return all books by Tolstoy.
        #If no query is given:
        #Fetch all books

    return render(request, 'store/book_list.html', {
        'books': books,
        'query': query,
    })
#Render the template store/book_list.html.
#Pass a context dictionary with:
#'books': the list of books (either filtered or all).
#'query': the search term the user entered (so it can be displayed again in the search bar).
#The result is an HTML page shown to the user with the list of books.
