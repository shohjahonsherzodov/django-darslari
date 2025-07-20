from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)  
    tags = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
                   
    def __str__(self):
        return self.title

