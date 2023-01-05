# Generated by Django 4.1.4 on 2022-12-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_category_women_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Изветные женщины', 'verbose_name_plural': 'Изветные женщины'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_publisher',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Ф И О'),
        ),
    ]
