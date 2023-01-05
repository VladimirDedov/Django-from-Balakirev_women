from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Ф И О')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_publisher =  models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            null=True)  # Внешний ключ с классом(таблицей) Categoryp

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # формирование маршрута по правилу из url.py для post
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Изветные женщины'  # отображение для единственного числа в админке
        verbose_name_plural = 'Изветные женщины'  # отображение для множественного числа в админке
        ordering = ['time_create', 'title']  # сортировка отображения записей в админке в админке и на сайте


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # формирование маршрута по правилу из url.py для post
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'  # отображение для единственного числа
        verbose_name_plural = 'Категории'  # отображение для множественного числа
        ordering = ['id']
