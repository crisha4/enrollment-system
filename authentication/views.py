from django.shortcuts import render

def main(request):
    return render(request, "authentication/base.html",{})

def login(request):
    return render(request, "authentication/login.html",{})

def register(request):
    return render(request, "authentication/register.html",{})

def home(request):
    return render(request, "authentication/home.html",{})

def logout(request):
    pass