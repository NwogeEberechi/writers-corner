from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Article, CustomUser
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
    authentication_classes = ()
    permission_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class Login(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)