from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    isbn = models.IntegerField()

    def __str__(self):
        return self.title