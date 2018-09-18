from django.urls import path

from .views import Index, ArticleList, ArticleDetail, UserList, UserDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('articles', ArticleList.as_view(), name='news'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='news_details'),
    path('users', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_details')
]