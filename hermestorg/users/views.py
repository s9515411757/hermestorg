from django.shortcuts import render, redirect

from .forms import LoginForm
from .models import User


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # flag_legal_entity = form.cleaned_data['flag_legal_entity']
            # ogrn = form.cleaned_data['ogrn']
            # document = form.cleaned_data['document']
            form.save()
            return redirect('home:index')

    form = LoginForm()

    return render(request, 'users/login.html', {'form': form})