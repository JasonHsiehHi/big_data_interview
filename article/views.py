from article.models import Article, Author, Publisher, ImageObject
from article.serializers import ArticleSerializer, AuthorSerializer, PublisherSerializer, ImageObjectSerializer
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ImageObjectViewSet(viewsets.ModelViewSet):
    queryset = ImageObject.objects.all()
    serializer_class = ImageObjectSerializer

