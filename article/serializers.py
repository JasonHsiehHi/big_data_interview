from rest_framework import serializers
from article.models import Article, Author, Publisher, ImageObject


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class ImageObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageObject
        fields = '__all__'

