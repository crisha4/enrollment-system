from django.urls import path
from . import views
# . (dot) means current directory

urlpatterns = [
    path('', views.land, name='authentication-land'),
    path('login/', views.login, name='authentication-login'),
    path('register/', views.register, name='authentication-register'),
]