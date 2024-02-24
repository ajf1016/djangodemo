from django.shortcuts import render
from django.http.response import HttpResponse


def htmlPage(request):
    name = "Juog548"
    context = {
        "name" : name
    }
    return render(request, 'index.html',context=context)

def aboutPage(request):
    return render(request, 'about.html')
