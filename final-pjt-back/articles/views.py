from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer


# 게시글 리스트
@api_view(["GET", "POST"])
def article_list_or_create(request):
    def article_list():
        articles = get_list_or_404(Article)[::-1]
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    
    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        return article_list()
    elif request.method == "POST":
        return create_article()


# 게시글 상세 정보, 업데이트, 삭제 
@api_view(['GET', 'PUT', "DELETE"])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer =  ArticleListSerializer(article)
        return Response(serializer.data)

    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "GET":
        return article_detail()
    elif request.method == "PUT":
        if request.user == article.user:
            return update_article()
    elif request.method == "DELETE":
        if request.user == article.user:
            return delete_article()


# 게시글에 대한 좋아요
@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.article_like.filter(pk=user.pk).exists():
        article.article_like.remove(user)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    else:
        article.article_like.add(user)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)


# 각 게시글에 대한 댓글 리스트, 댓글 생성
@api_view(['GET', 'POST'])
def comment_list_or_create(request, article_pk):

    def comment_list():
        comments = get_list_or_404(Comment, article=article_pk)[::-1]
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create_comment():
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

    if request.method == 'GET':
        return comment_list()
    elif request.method == "POST":
        return create_comment()


# 각 게시글의 댓글 수정 및 삭제
@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        if request.user == comment.user:
            return update_comment()
    elif request.method == "DELETE":
        if request.user == comment.user:
            return delete_comment()


@api_view(['POST'])
def comment_article_like(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if comment.comment_like.filter(pk=user.pk).exists():
        comment.comment_like.remove(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.comment_like.add(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
