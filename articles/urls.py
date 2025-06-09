# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),  # Страница списка статей
    path('create/', views.article_create, name='create'),  # Страница создания статьи
    path('<slug:slug>/', views.article_item, name='article_detail'),  # Статья по slug
    path('update/<slug:slug>', views.article_update, name='update'),
    path('delete/<slug:slug>', views.article_delete, name='delete'),

]
