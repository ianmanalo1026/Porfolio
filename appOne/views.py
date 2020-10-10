from django.shortcuts import render
from django.http import HttpResponse
from .models import Content


def home(request):
    content = Content.objects.all()
    return render(request, 'appOne/home.html', {'content':content})