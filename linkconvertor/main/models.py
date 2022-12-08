from django.db import models

class Link(models.Model):
    objects = None
    original_url = models.CharField('Исходная ссылка', max_length=1000)
    shortlink_url = models.CharField('Сокращенная ссылка', max_length=6)

    class Meta:
        verbose_name = 'Cсылка'
        verbose_name_plural = 'Cсылки'
