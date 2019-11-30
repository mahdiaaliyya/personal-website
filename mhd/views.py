from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def homepage(request):
    return render(request, 'index.html')
