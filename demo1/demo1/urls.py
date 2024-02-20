from django.contrib import admin
from django.urls import path
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

urlpatterns = [
    path('admin/', admin.site.urls),
]
