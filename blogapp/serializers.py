from rest_framework import serializers
from .models import ArticleList

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleList
        fields = ['id', 'title','author', 'body']