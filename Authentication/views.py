from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users

@unauthenticated_user

def login_user(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        password = request.POST.get('password')
        username = request.session.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {}
            return render(request, 'introduction.html', context)
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html')
    

    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')