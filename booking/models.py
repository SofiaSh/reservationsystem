from django.db import models
from persons.models import Person
from resourses.models import Resourse


class Booking(models.Model):
    """Модель реализует сущность резервируемого объекта"""
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    #resourse = models.ForeignKey(Resourse, on_delete=models.CASCADE)

    resourse = models.TextField(verbose_name='ресурс', max_length=2000)
    start_time = models.DateTimeField(verbose_name="Время начала", default='00:00')
    end_time = models.DateTimeField(verbose_name="Время окончания", default='00:01')

    class Meta:
        db_table = 'Booking'
        verbose_name = 'бронь'
        verbose_name_plural = 'брони'
