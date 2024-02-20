from django.shortcuts import render
from django.http.response import HttpResponse


def webIndex(request):
    return HttpResponse("Hello World!, from Web app<a href='http://127.0.0.1:8000/web/'>Click for web page</a>")

def htmlPage(request):
    return render(request, 'index.html')
