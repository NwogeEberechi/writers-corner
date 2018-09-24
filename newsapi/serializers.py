from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'text', 'author','pk')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last_name', 'pk')
