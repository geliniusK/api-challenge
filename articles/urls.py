from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    ArticleList,
    ArticleDetail,
    AdminArticleViewSet,
    AdminAuthorViewSet
    )

router = SimpleRouter()
router.register('admin/articles', AdminArticleViewSet)
router.register('admin/authors', AdminAuthorViewSet)

urlpatterns = [
    path('articles/<uuid:pk>/', ArticleDetail.as_view()),
    path('articles/', ArticleList.as_view()),
]

urlpatterns += router.urls
