import http.client
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Post


def index(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')


def blog(request):
    blog_posts = Post.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})


def contactus(request):
    return render(request, 'contacts.html')


def money(request):
    return render(request, 'money.html')


def about(request):
    return render(request, 'about.html')


def money(request):
    return render(request, 'money.html')


def projects(request):
    return render(request, 'projects.html')


def team(request):
    return render(request, 'team.html')


def news(request):
    return render(request, 'news.html')


def carieers(request):
    return render(request, 'carieers.html')


def carierdes(request):
    return render(request, 'carierdes.html')


def newsDsc(request):
    return render(request, 'newsDsc.html')
