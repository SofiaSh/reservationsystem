# Generated by Django 2.2.2 on 2019-06-23 06:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190623_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 23, 12, 31, 11, 397776), verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='resourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='resourses.Resourse'),
        ),
    ]
