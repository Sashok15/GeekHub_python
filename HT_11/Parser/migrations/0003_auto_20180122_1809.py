# Generated by Django 2.0.1 on 2018-01-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parser', '0002_askstories_jobstories_newstories_showstories'),
    ]

    operations = [
        migrations.AddField(
            model_name='askstories',
            name='kids',
            field=models.TextField(default='kids'),
        ),
        migrations.AddField(
            model_name='askstories',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='askstories',
            name='text',
            field=models.TextField(default='text'),
        ),
        migrations.AddField(
            model_name='askstories',
            name='time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='askstories',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]