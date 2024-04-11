from django.shortcuts import render

from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        pass

    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})