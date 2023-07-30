from django.urls import path
from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page, never_cache

from blog.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('clients/', ArticleListView.as_view(), name='article_list'),
    path('clients/create/', never_cache(ArticleCreateView.as_view()), name='article_create'),
    path('clients/update/<int:pk>/', never_cache(ArticleUpdateView.as_view()), name='article_update'),
    path('clients/delete/<int:pk>/', never_cache(ArticleDeleteView.as_view()), name='article_delete'),
    path('clients/<int:pk>/', cache_page(60)(ArticleDetailView.as_view()), name='article_detail'),
]