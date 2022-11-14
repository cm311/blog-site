import datetime

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Article(models.Model):
    BOOKREVIEW = 'BOOK'
    ARTICLE = 'ARTICLE'
    SOFTWARE = 'SOFTWARE'
    GAMING = 'GAMING'
    LANGUAGE = 'LANGUAGE'
    FICTION = 'FICTION'

    tag_types = [
        (BOOKREVIEW, 'Book Review'),
        (ARTICLE, 'Article'),
        (SOFTWARE, 'Software'),
        (GAMING, 'Gaming'),
        (LANGUAGE, 'Language'),
        (FICTION, 'Fiction'),
    ]

    article_title = models.CharField(max_length=600)
    date = models.DateTimeField('date published', default=datetime.datetime.now())
    tag = models.CharField(choices=tag_types, default=ARTICLE, max_length=100)
    body = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField('date published')
    userID = models.TextField(default='Anonymous')
    body = models.TextField()
