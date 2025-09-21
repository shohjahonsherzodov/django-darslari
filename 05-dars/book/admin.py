from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview

class BooksAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'description', 'isbn')
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', )

admin.site.register(Book, BooksAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
admin.site.register(Author, AuthorAdmin)
