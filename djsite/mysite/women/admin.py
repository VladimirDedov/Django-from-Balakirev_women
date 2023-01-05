from django.contrib import admin

from .models import *


# Класс для отображения дополнительных полей в админ панеле
class WomenAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'time_create', 'photo', 'is_publisher')  # Список полей, которые будут отображаться в админ панеле
    list_display_links = ('id', 'title')  # поля на которые можно кликнуть для перехода на статью
    search_fields = ('title', 'content')  # по каким полям производить поиск
    list_editable = ('is_publisher',)#чтобы поле было редактируемым в админке, не заходя в карточку.(Удобно для Boolean)
    list_filter = ('is_publisher', 'time_create')# Поля по которым можно сортировать в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name')  # Список полей, которые будут отображаться в админ панеле
    list_display_links = ('id', 'name')  # поля на которые можно кликнуть для перехода на статью
    search_fields = ('name',)  # по каким полям производить поиск


admin.site.register(Category, CategoryAdmin)# прописать вторым вспомогательный класс. Обязательно.
admin.site.register(Women, WomenAdmin)  # прописать вторым вспомогательный класс. Обязательно.
