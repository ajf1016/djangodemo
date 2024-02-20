from django.urls import path
from web.views import webIndex,htmlPage


urlpatterns = [
    path('', webIndex),
    path('web/', htmlPage)
]
