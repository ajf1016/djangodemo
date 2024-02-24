from django.shortcuts import render
from django.http.response import HttpResponse


def htmlPage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html')
