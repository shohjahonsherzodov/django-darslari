from django.shortcuts import render
from django.views import View
from book.models import Book
class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})

class BookDetail(View):
    def get(self, request, id):
        books = Book.objects.get(id=id)
        return render(request, 'books/detail.html', {'books': books})
