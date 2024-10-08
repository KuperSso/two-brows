# Generated by Django 4.2.1 on 2024-08-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diplomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/diplomas/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Диплом',
                'verbose_name_plural': 'Дипломы',
                'db_table': 'diplomas',
            },
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/me/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'домашнюю страницу',
                'verbose_name_plural': 'Домашняя страница',
                'db_table': 'welcome',
            },
        ),
    ]
