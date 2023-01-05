from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .forms import AddPostForm
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):  # ссылка на класс HttpRequest
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': "Head Page",
               'cat_selected': 0}

    return render(request, 'women/index.html',
                  context=context)  # именнованому параметру context присваеваем ссылку на словарь context


def show_post(request, post_id):
    post = Women.objects.get(pk=post_id)
    cats = Category.objects.all()
    context = {'post': post,
               'cats': cats,
               'menu': menu,
               'title': post.title,
               }

    return render(request, 'women/post.html',
                  context=context)


def about(request):  # ссылка на класс HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': "About site"})


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': "Head Page",
               'cat_selected': cat_id}
    if len(posts) == 0:
        raise Http404()

    return render(request, 'women/index.html',
                  context=context)  # именнованому параметру context присваеваем ссылку на словарь context


def categories(request, cat):
    return HttpResponse(f'<h1>Topic for categories</h1><p>{cat}</p>')


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():  # Данные прошли валидацию
            form.save()  # Сохрание данных в базе данных
            return redirect('home')
    else:
        form = AddPostForm()
    cats = Category.objects.all()

    context = {
        'form': form,
        'cats': cats,
        'menu': menu,
        'title': "Add Page"
    }
    return render(request, 'women/addpage.html',
                  context=context)


def contact(requests):
    return HttpResponse('Contact')


def login(requests):
    return HttpResponse('Login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h2>')
