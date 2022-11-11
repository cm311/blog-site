from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'tag']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['article']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)