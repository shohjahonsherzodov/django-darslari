from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    isbn = models.IntegerField(max_length=13)
    price = models.IntegerField()