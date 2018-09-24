from django.db import models
from django.utils import	timezone
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey('auth.User',	on_delete=models.CASCADE)
    title =	models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(null=True, default=timezone.now)
    
    def	__str__(self):
        return	self.title
