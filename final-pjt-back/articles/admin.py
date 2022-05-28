from django.contrib import admin
from .models import Article, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at', 'post_hit', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'user', 'content', 'created_at', )



admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)