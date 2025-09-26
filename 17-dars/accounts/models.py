from django.db import models

class RegisterModel(models.Model):
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=16)
