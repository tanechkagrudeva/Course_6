from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'views', 'published_at',)
    list_filter = ('title', 'views', 'published_at',)
