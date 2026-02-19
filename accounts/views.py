from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("login")
    return render(request, "accounts/signup.html")

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("product_list")
    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
