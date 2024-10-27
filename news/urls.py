from django.urls import path
from .views import *


app_name = 'news'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    
    
]
