from django.contrib import admin
from django.urls import path
from devideosapp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('watch', views.watchpage, name='watch'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
]
