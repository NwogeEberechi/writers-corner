from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article, CustomUser


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'is_active')

        def create(self):
            user = CustomUser(
                email='email',
                username='username',
                password='password',
                is_active=1
            )
            user.save()
            Token.objects.create(user=user)
            return user
