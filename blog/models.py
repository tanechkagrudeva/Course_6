from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')
    published_at = models.DateField(verbose_name='дата публикации')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

