from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Content
from django.contrib.auth.models import User


def home(request):
    content = Content.objects.all()
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == "POST":
        if not name and not email and not message:
            content = 'name: ' + name + '\n' + 'email: ' + email + '\n' + '\n' + message
            send_mail('Email from Portfolio', content, 'ian.manalo1026@gmail.com', ['ian.manalo1026@gmail.com'], fail_silently=False)
            return redirect('home')
    else:
        return render(request, 'appOne/home.html', {'content':content})