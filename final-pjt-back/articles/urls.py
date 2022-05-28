
from django.urls import path
from . import views

urlpatterns = [
    # article
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.like_article),

    # comment
    path('<int:article_pk>/comments/', views.comment_list_or_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.comment_article_like), # 영화 댓글에 대한 좋아요


]
