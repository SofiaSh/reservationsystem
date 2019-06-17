# Generated by Django 2.2.2 on 2019-06-16 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
        ('resourses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='resourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourses.Resourse'),
        ),
    ]
