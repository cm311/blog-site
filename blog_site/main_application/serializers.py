from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Article
        fields = ['article_title', 'date', 'body', 'tag']


class CommentSerializer(serializers.ModelSerializer):

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Comment
        fields = ['date', 'userID', 'body']