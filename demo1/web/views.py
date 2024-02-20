from django.shortcuts import render
from django.http.response import HttpResponse


def webIndex(request):
    return HttpResponse("Hello World!, from Web app")

