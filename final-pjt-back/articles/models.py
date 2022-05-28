from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post_hit = models.PositiveIntegerField(default=0)
    article_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)


    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    comment_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments", blank=True)

    def __str__(self):
        return self.content