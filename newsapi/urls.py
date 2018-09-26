from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import Index, UserArticle, UserViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name="my_users")
router.register(r'articles', ArticleViewSet, base_name='my_articles')

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('user/<int:pk>/articles/', UserArticle.as_view(), name='user_article'),
]

urlpatterns += router.urls