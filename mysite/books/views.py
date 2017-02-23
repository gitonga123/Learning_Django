from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.


def search_form(request):
    return render(request,'search_form.html')


def search(request):
    error = []
    if 'search_box' in request.GET:
        search_box = request.GET['search_box']
        if not search_box:
            error.append('Enter a search term.')
        elif len(search_box) > 20:
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=search_box)
            return render(request,'search_results.html',{'books': books,'query': search_box})
    else:
        return render(request,'search_form.html', {'error': error})



