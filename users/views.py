from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    return render(request, "profile.html")


def login(request):
    if request.user.is_authenticated:
        return HttpResponse("Siz allaqachon tizimga kirib bo'lgansiz!")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("profile")
        else:
            return HttpResponse("Username yoki parol noto'g'ri")
        
    return render(request, "login.html")

def logout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            auth_logout(request)
            return redirect("profile")
        return render(request, "logout.html")
    else:
        return HttpResponse("Siz allaqachon tizimdan chiqib ketib bo'lgansiz!")

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        has_error = False

        if User.objects.filter(email=email):
            messages.error(request, "Ushbu email bilan foydalanuvchi mavjud")
            has_error = True

        if User.objects.filter(username=username):
            messages.error(request, "Ushbu username bilan foydalanuvchi mavjud")

        if password1 != password2:
            messages.error(request, "Parollar o'zaro bir xil emas")
            has_error=True

        if len(password1) < 8 :
            messages.error(request, "Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
            has_error=True

        if not has_error:
            user = User.objects.create(email=email, username=username, first_name=first_name, last_name=last_name)
            user.set_password(password1)
            user.save()
            return redirect("profile")
        else:
            pass
    return render(request, "register.html")

@login_required(login_url="login")
def user_update(request):
    user = request.user
    