from rest_framework import serializers
from .models import Article, Author


class ArticleGETSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'category', 'title', 'summary')
        depth = 1


class ArticleAnonDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'category', 'title', 'summary', 'firstParagraph')


class ArticleLoggedDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'category', 'title', 'summary', 'firstParagraph',
            'body')


class ArticlePOSTSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'category', 'title', 'summary', 'firstParagraph',
            'body')
        depth = 1


class AuthorPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name', 'picture')
