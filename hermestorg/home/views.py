from django.shortcuts import render


def index(request):
    data = {
        'title': 'Привет! Лев'
    }
    return render(request, 'home/index.html', data)