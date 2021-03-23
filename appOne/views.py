from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import FormView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import Content
from .forms import ContentForm


def home(request):
    content = Content.objects.all()
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == "POST":
        if not name and not email and not message:
            content = 'name: ' + name + '\n' + 'email: ' + email + '\n' + '\n' + message
            send_mail('Email from Portfolio', content, 'ian.manalo1026@gmail.com', ['ian.manalo1026@gmail.com'], fail_silently=False)
            messages.success(request, "Your Email has been sent")
            return redirect('home')
    else:
        return render(request, 'appOne/home.html', {'content':content})
    

class UserSignInView(FormView):
    """Authentication for user"""
    model = User
    form_class = AuthenticationForm
    template_name = 'appOne/signin.html'
    success_url = '/'
    

class CreateContentView(CreateView):
    form_class = ContentForm
    template_name = 'appOne/create_content.html'