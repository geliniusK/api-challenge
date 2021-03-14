from django.contrib import admin

from .models import Article, Author
#
# class ReviewInline(admin.TubularInline):
#     model = Article
admin.site.register(Article)
admin.site.register(Author)
# Register your models here.
