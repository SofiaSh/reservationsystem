from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    """Класс расширяет стандартную модель User, добавлены поля для отчества и
    биографии
    """
    patronymic = models.CharField(verbose_name='отчество', max_length=30,
                                  default='')
    biography = models.TextField(verbose_name='биография', max_length=2000,
                                 default='')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Persons'
        verbose_name = 'персона'
        verbose_name_plural = 'персоны'
