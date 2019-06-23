from django.db import models
from persons.models import Person
from resourses.models import Resourse
from datetime import datetime,  timedelta


class Booking(models.Model):
    """Модель реализует сущность резервируемого объекта"""
    owner = models.ForeignKey(Person, related_name='booking', on_delete=models.CASCADE)
    resourse = models.ForeignKey(Resourse, related_name='booking',  on_delete=models.CASCADE)

    start_time = models.DateTimeField(verbose_name="Время начала", default=datetime.now)
    end_time = models.DateTimeField(verbose_name="Время окончания", default=datetime.now() - timedelta(hours = 1))

    class Meta:
        db_table = 'Booking'
        verbose_name = 'бронь'
        verbose_name_plural = 'брони'
