from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title
