from django.shortcuts import render
from django.core.mail import send_mail
from .models import Content


def home(request):
    content = Content.objects.all()
    return render(request, 'appOne/home.html', {'content':content})

def send_email(request):
    send_mail('test',
              'test',
              'ian.manalo1026@gmail.com',
              ['ian.manalo1026@gmail.com'], 
              fail_silently=False)
    return render(request,'appOne/send.html')