from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    published_at = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def views_count(self):
        self.views += 1
        self.save()

