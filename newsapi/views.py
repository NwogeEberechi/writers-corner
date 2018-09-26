from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.status import HTTP_401_UNAUTHORIZED

from .models import Article
from  .serializers import ArticleSerializer, UserSerializer

# Create your views here.
class Index(APIView):
    def get(self, request):
        data = {"details": "Welcome to Writers-Corner news api"}
        return Response(data)

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        data = UserSerializer(queryset, many=True).data
        return Response(data)
    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        data = UserSerializer(user).data
        return Response(data)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def destroy(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author.id != request.user.id:
            return Response(
                data='The article you want to delete belongs to another user! You are only permitted to delete ONLY your article!',
                status=HTTP_401_UNAUTHORIZED
                )
        article.delete()
        return Response(data={"detail": "Successfully deleted"})

class UserArticle(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        queryset = user.article_set.all()
        data = ArticleSerializer(queryset, many=True).data
        return Response(data)