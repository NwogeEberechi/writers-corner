from django.urls import path

from .views import Index, ArticleList, ArticleDetail, Signup

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('articles', ArticleList.as_view(), name='news'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='news_details'),
    path('signup', Signup.as_view(), name='create_user')
]