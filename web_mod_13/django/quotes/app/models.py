from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    fullname = models.CharField()
    born = models.CharField()
    location = models.CharField(max_length=100, null=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Quotes(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)