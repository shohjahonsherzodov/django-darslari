from django.contrib import admin
from .models import Book, BookAuthor, Author, BookReview

admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Author)
admin.site.register(BookReview)
