from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.TextField(blank=True)
    

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# class Comment(models.Model):
#     profile = models.ForeignKey(Profile, related_name="commentsasdasd", on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="commentsasdasd", on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.content