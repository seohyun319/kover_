# Generated by Django 3.1.5 on 2021-02-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kover', '0009_auto_20210206_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='show_times',
        ),
        migrations.AddField(
            model_name='show',
            name='show_times',
            field=models.ManyToManyField(related_name='show_time', to='kover.Time'),
        ),
    ]