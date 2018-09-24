from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

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

class Users(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserArticle(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        queryset = user.article_set.all()
        data = ArticleSerializer(queryset, many=True).data
        return Response(data)