from django.shortcuts import render


def index(request):
    data = {
        'title': 'Тестовый текст'
    }
    return render(request, 'home/index.html', data)