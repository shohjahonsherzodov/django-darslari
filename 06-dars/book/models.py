from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    isbn = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return F"{self.first_name} {self.last_name}"
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey( Author, on_delete=models.CASCADE)
class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.IntegerField(
        validators = (MinLengthValidator(1), MaxLengthValidator(5))
    )