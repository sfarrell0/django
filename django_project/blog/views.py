from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'Sam Farrell',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',

    },
    {
        'author': 'Gregor Watson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 24, 2024',

    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT PAGE'})
