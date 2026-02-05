
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    slug = models.SlugField(unique=True)  

    def __str__(self):
        return self.title
