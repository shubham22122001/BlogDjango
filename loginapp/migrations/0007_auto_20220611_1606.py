# Generated by Django 3.2.13 on 2022-06-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_auto_20220611_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_data1',
            name='is_draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
        migrations.AddField(
            model_name='blog_data1',
            name='is_publish',
            field=models.BooleanField(default=False, verbose_name='Publish'),
        ),
    ]
