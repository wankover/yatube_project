

from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    context = {'title' : title,
               'text' : text,
               }
    return render(request, template, context)

def group_posts(request, slug):
    text = 'Здесь будет информация о группах проекта Yatube'
    title = 'Лев Толстой – зеркало русской революции.'
    context = {'title' : title,
               'text' : text,
               }
    template = 'posts/group_list.html'
    
    return render(request, template, context)
