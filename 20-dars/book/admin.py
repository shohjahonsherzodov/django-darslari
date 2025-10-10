from django.contrib import admin

from .models import Book, BookAuthor, Author, BookReview
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title', 'description')
    list_display = ('id', 'title', 'description', 'author', 'isbn', 'price')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('id', 'first_name', 'last_name')
    list_display = ('id', 'first_name', 'last_name', 'bio', 'email')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview)
admin.site.register(BookAuthor)

