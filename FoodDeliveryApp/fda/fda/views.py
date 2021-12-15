from django.http.response import Http404
from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username must be unique")
            return redirect('index')
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('index')
        user = User.objects.create_user(username, email, password1)
        user.name = name
        user.save()
        messages.success(request, "Hi " + name + ", Welcome to Foodie!")
        return redirect('/foodie')
    else:
        return redirect('index')

def user_login(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/foodie')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('index')
    else:
        return redirect('index')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')