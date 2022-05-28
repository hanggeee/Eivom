from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
# from .models import Comment
from movies.serializers import MovieSerializer
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('id','username','email', 'profile_img', 'followings', 'followers', 'like_movies')

class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'id')

# class CommentSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#             class Meta:
#                 model = User
#                 fields = ('pk', 'username', 'profile_img')

#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Comment
#         fields = ('pk', 'user', 'content', 'profile', 'created_at',)
#         read_only_fields = ('profile',)
    