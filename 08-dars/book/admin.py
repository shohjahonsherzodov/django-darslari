from django.contrib import admin

from .models import Book, BookAuthor, BookReview, Author

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'isbn')
    list_display = ('title', 'description', 'isbn', 'price')
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'bio', 'email')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview)
admin.site.register(BookAuthor)