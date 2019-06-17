from django.db import models


class Resourse(models.Model):
    """Модель реализует сущность резервируемого объекта"""
    headline = models.CharField(verbose_name='заголовок', max_length=120, default=' ')
    description = models.TextField(verbose_name='описание', max_length=2000)

    def __str__(self):
        return self.headline

    class Meta:
        db_table = 'Resourses'
        verbose_name = 'ресурс'
        verbose_name_plural = 'ресурсы'

