from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profile_img')


class ArticleLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',)

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username', 'profile_img')

    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article', 'created_at', 'updated_at')
        read_only_fields = ('article',)

class ArticleListSerializer(serializers.ModelSerializer):
    
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ('pk')
    user = UserSerializer(read_only=True)
    article_like = ArticleLikeListSerializer(read_only=True, many=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id','pk', 'title', 'content', 'created_at', 'updated_at', 'post_hit', 'user', 'article_like', 'comments')


class ArticleSerializer(serializers.ModelSerializer):
    article_like = ArticleLikeListSerializer(read_only=True, many=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'created_at', 'updated_at', 'post_hit', 'article_like', 'comments')



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('article', 'user')







