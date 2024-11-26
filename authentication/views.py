from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# from .models import Post


def land(request):
  return render(request, 'authentication/land.html', {})

def login(request):
  return render(request, 'authentication/login.html', {})

def home(request):
  return render(request, 'authentication/home.html', {})

def register(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()  # Save the form to create a new user
      return redirect('login')  # Redirect to the login page after successful registration
  else:
    form = CustomUserCreationForm()

  return render(request, 'authentication/register.html', {'form': form})