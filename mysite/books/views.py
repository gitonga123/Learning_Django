from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.


def search_form(request):
    return render(request,'search_form.html')


def search(request):
    if 'search_box' in request.GET:
        message="You Searched for: %r " % request.GET['search_box']
        search_box = request.GET['search_box']

        books = Book.objects.filter(title__icontains=search_box)

        return render(request,'search_results.html',{'books': books,'query': search_box})
    else:
        return render(request,'search_form.html', {'error': True})



