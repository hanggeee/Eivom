from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.genre_name)


class Movie (models.Model):
    movie_id = models.IntegerField(unique=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)

    def __str__(self):
        return str(self.movie_id)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    movie_comment_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie_comments", blank=True)


    # def __str__(self):
    #     return self.user // 적용하면 __str__ 에러남