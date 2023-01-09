from django.db.models import Count

from .models import Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

class Datamixin:
    def get_user_context(self, **kwargs):  # Функция для формирования стат и изменяемых данных для шаблона. Список context
        context = kwargs
        context['menu'] = menu
        context['cats'] = Category.objects.annotate(Count('women')).order_by('name')
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context