from django.shortcuts import render
from django.views import View
from .models import Book

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'books' : books
        }
        
        return render(request, 'book/list.html', context)

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            'book' : book
        }

        return render(request, 'accounts/detail.html', context)
    
