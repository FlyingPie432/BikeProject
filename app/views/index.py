import http.client

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.models import Post
from django.urls import reverse


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


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject='Message from Volti Website',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email=email,
            recipient_list=['your_email@example.com'],
            fail_silently=False,
        )
        messages.success(request, 'Email successfully sent!')
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'contacts.html')
