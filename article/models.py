from django.db import models


class Article(models.Model):
    type = models.CharField(max_length=10)  # Daily or Popular
    content = models.JSONField()  # depends on type. Daily: list form, Popular: dict form
    headline = models.TextField()
    image = models.ForeignKey('ImageObject', null=True, blank=True, on_delete=models.SET_NULL, default=None)

    datePublished = models.DateTimeField(null=True, blank=True)
    dateModified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL, default=None)
    publisher = models.ForeignKey('Publisher', null=True, blank=True, on_delete=models.SET_NULL, default=None)

    description = models.TextField()

    url = models.URLField(max_length=200)
    thumbnailUrl = models.URLField(max_length=200)

    dateCreated = models.DateTimeField(auto_now_add=True)
    articleSection = models.CharField(max_length=5)
    creator = models.CharField(max_length=25)
    keywords = models.JSONField(null=True, blank=True, default=list)


class Author(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=10)


class Publisher(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    url = models.URLField(max_length=200)
    logo = models.ForeignKey('ImageObject', null=True, blank=True, on_delete=models.SET_NULL, default=None)


class ImageObject(models.Model):
    url = models.URLField(max_length=200)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

