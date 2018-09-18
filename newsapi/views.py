from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Article
from  .serializers import ArticleSerializer, UserSerializer

# Create your views here.
class Index(APIView):
    def get(self, request):
        data = 'Hello World'
        return Response(data)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer