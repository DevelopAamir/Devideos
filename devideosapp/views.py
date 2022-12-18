from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html');


def watchpage(request):
    return render(request, 'watchpage.html',{'title' : 'Flutter Project Best'});


def profile(request):
    return render(request, 'profile.html',{'title' : 'Codectionary - Online Learning Channel'});


def login(request):
    return render(request, 'login.html',{'title' : 'Codectionary - Online Learning Channel'});