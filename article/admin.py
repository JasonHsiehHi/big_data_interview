from django.contrib import admin
from article.models import Article, Author, Publisher, ImageObject


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageObject)
class ImageObjectAdmin(admin.ModelAdmin):
    pass
