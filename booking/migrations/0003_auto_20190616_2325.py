# Generated by Django 2.2.2 on 2019-06-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190616_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='resourse',
            field=models.TextField(max_length=2000, verbose_name='ресурс'),
        ),
    ]
