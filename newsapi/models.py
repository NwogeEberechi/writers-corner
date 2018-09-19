from django.db import models
from django.utils import	timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Article(models.Model):
    author = models.ForeignKey('CustomUser',	on_delete=models.CASCADE)
    title =	models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def	__str__(self):
        return	self.title
