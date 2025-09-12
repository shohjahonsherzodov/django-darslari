from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    cover_image = models