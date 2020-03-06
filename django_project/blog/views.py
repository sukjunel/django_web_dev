from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('<h1>blog home</h1>')
    return render(request, 'blog/home.html')


def about(request):
    # return HttpResponse('<h1>blog about</h1>')
    return render(request, 'blog/about.html')