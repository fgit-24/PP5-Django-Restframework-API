from django.db import models
from django.contrib.auth.models import User
from django import Pillow

# Create your models here.

class Porfile(models.Model):
    owner = models.OneToOneField(User, on_delete=Models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.CharField(blank=True)
    image = models.ImageField(
        upload_to='images/', default = '../pp5-walkthrough/botfh2hlxd6cudukcqj6.jpg'
    )

    class Meta:
        ordering = ['created_at']

    
    def __str__(self):
        return f"{self.owner}s' profile"