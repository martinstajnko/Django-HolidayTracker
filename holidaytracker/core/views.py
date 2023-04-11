from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('core:index')
            
        else:
            print('Username OR password is incorrect')
            messages.error(request, 'Username OR password is incorrect')
            return redirect('core:index')
        
    else:
        return render(request, 'core/index.html')


def logout(request):
    pass