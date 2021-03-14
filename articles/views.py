from django.contrib.auth.models import AnonymousUser
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import Article, Author
from .serializers import (
        ArticleGETSerializer,
        ArticlePOSTSerializer,
        ArticleAnonDetailSerializer,
        ArticleLoggedDetailSerializer,
        AuthorPOSTSerializer
        )


class ArticleList(generics.ListAPIView):

    serializer_class = ArticleGETSerializer

    def get_queryset(self):
        try:
            query = self.request.GET.get('category')
            queryset = Article.objects.filter(category__icontains=query)
            return queryset
        except ValueError:
            queryset = Article.objects.all()
            return queryset


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleAnonDetailSerializer
    serializer_logged_class = ArticleLoggedDetailSerializer

    def get_serializer_class(self):
        if not isinstance(self.request.user, AnonymousUser):
            return self.serializer_logged_class
        else:
            return super().get_serializer_class()


class AdminArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.all()
    serializer_class = ArticlePOSTSerializer


class AdminAuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorPOSTSerializer
