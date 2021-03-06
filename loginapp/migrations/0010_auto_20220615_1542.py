# Generated by Django 3.2.13 on 2022-06-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='book1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('speciality', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='book',
        ),
    ]
