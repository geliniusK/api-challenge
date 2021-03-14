import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=50)
    firstParagraph = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
