from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_display = ('id', 'title', 'description', 'author', 'isbn', 'price')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('id', 'first_name', 'last_name', 'email', 'bio')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)