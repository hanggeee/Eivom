from django.contrib import admin
from .models import Genre, Movie, Comment
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_id', 'genre_name', )

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'movie_id', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'rate', 'movie', 'user',)



admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)