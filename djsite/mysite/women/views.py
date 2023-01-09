from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *
from .utils import *




# Класс предаставления главной страницы WomenHome

class WomenHome(Datamixin, ListView):  # Класс для представления начаьной страницы
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None,
                         **kwargs):  # Функция для формирования стат и изменяемых данных для шаблона. Список context
        context = super().get_context_data(**kwargs)  # Получения списка данных из родительского класса ('posts)
        # context['menu'] = menu
        # context['cats'] = Category.objects.all()
        # context['title'] = 'Home'
        # context['cat_selected'] = 0
        c_def=self.get_user_context(title='Home')#получаем словарь из Миксина
        context.update(c_def)#Объединение двух словарей для шаблона
        return context

    def get_queryset(self):  # Специальный метод для возврата данных из БД выше. model = Women
        return Women.objects.filter(is_publisher=True).order_by('-time_create')


# def index(request):  # ссылка на класс HttpRequest
#     posts = Women.objects.all()
#     cats = Category.objects.all()
#     context = {'posts': posts,
#                'cats': cats,
#                'menu': menu,
#                'title': "Head Page",
#                'cat_selected': 0}
#
#     return render(request, 'women/index.html',
#                   context=context)  # именнованому параметру context присваеваем ссылку на словарь context

# Класс представления категорий ShowCategory
class ShowCategory(Datamixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # Если ни одного поста не выбрано, то генерируется ошибка

    def get_context_data(self, *, object_list=None, context=None, **kwargs):  # Функция для формирования стат и изменяемых данных для шаблона. Список context
        context = super().get_context_data(**kwargs)  # Получения списка данных из родительского класса ('posts)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        context.update(c_def)
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_publisher=True).order_by('-time_create')  # cat__slug - обращение к связанной БД Category


# def show_category(request, cat_slug):
#     posts = Women.objects.filter(cat__slug=cat_slug)
#     cats = Category.objects.all()
#     context = {'posts': posts,
#                'cats': cats,
#                'menu': menu,
#                'title': "Head Page",
#                'cat_selected': cat_slug}
#     if len(posts) == 0:
#         raise Http404()
#
#     return render(request, 'women/index.html',
#                   context=context)  # именнованому параметру context присваеваем ссылку на словарь context

#Класс представления поста ShowPost
class ShowPost(Datamixin,DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = 'post_slug'# Для переменной слага. Берется из файла url.py
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None,
                         **kwargs):  # Функция для формирования стат и изменяемых данных для шаблона. Список context
        context = super().get_context_data(**kwargs)  # Получения списка данных из родительского класса ('posts)
        c_def = self.get_user_context(title=context['post'])
        context.update(c_def)
        return context

# def show_post(request, post_slug):
#     post = Women.objects.get(slug=post_slug)
#     cats = Category.objects.all()
#     context = {'post': post,
#                'cats': cats,
#                'menu': menu,
#                'title': post.title,
#                }
#
#     return render(request, 'women/post.html',
#                   context=context)


def about(request):  # ссылка на класс HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': "About site"})


def categories(request, cat):
    return HttpResponse(f'<h1>Topic for categories</h1><p>{cat}</p>')

class AddPage(Datamixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')#перенаправление после добавления поста. Построение "ленивого " маршрута, когда понадобится
    def get_context_data(self, *, object_list=None,
                         **kwargs):  # Функция для формирования стат и изменяемых данных для шаблона. Список context
        context = super().get_context_data(**kwargs)  # Получения списка данных из родительского класса ('posts)
        c_def = self.get_user_context(title='Addpage')
        context.update(c_def)
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():  # Данные прошли валидацию
#             form.save()  # Сохрание данных в базе данных
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     cats = Category.objects.all()
#
#     context = {
#         'form': form,
#         'cats': cats,
#         'menu': menu,
#         'title': "Add Page"
#     }
#     return render(request, 'women/addpage.html',
#                   context=context)


def contact(requests):
    return HttpResponse('Contact')


def login(requests):
    return HttpResponse('Login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h2>')
