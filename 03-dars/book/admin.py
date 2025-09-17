from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview

class BooksAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'description', 'isbn')

admin.site.register(Book, BooksAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
admin.site.register(Author)
