# Generated by Django 3.1.5 on 2021-02-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kover', '0013_auto_20210207_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_intermission',
            field=models.TimeField(blank=True, verbose_name='공연 인터미션'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_runtime',
            field=models.TimeField(blank=True, verbose_name='공연 런타임'),
        ),
    ]
