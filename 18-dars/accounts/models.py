from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username
