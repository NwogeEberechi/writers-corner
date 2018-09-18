from django.urls import path

from .views import Index, ArticleList, ArticleDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('articles/', ArticleList.as_view(), name='news'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='news_details'),
]