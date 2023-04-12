from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):

    return render(request, 'core/home.html')


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('core:home')

        else:
            print('Username OR password is incorrect')
            messages.error(request, 'Username OR password is incorrect')
            return redirect('core:login')
        
    else:
        return render(request, 'core/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('core:login')