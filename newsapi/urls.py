from django.urls import path
from rest_framework.authtoken import views

from .views import Index, ArticleList, ArticleDetail, UserList, UserDetail, Login

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('articles', ArticleList.as_view(), name='news'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='news_details'),
    path('users', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_details'),
    #path("login", Login.as_view(), name="login"),
    path("login", views.obtain_auth_token, name="login"),
]