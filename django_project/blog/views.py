# 2. THIS is where we layout the page. We bring template into this page

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# #dummy data
# posts = [
#     {
#         'author': 'Sukjunel',
#         'title': 'how to become a good programmer',
#         'content': 'you just do it!',
#         'date_posted': 'Jun 25, 2000'
#     },
#     {
#         'author': 'June',
#         'title': 'how to become a bad programmer',
#         'content': 'wear adidas!',
#         'date_posted': 'Jun 25, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>blog home</h1>')
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})