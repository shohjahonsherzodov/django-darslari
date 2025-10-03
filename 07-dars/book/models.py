from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    isbn = models.IntegerField(max_length=15)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    bio = models.TextField()

    def __Str__(self):
        return f'{self.first_name} {self.last_name}'
    
class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

class BookReview(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.IntegerField(
        validators= (MinLengthValidator(1), MaxValueValidator(5))
    )