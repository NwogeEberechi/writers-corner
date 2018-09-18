from rest_framework import generics
from rest_framework.views import APIView

from .models import Article
from  .serializers import ArticleSerializer

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