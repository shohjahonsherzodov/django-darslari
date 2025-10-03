from django.contrib import admin
from .models import Book, BookAuthor, BookReview, Author

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'id')
    list_display = ('id', 'title', 'description', 'isbn', 'price')
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
