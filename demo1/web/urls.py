from django.urls import path
from web.views import webIndex


urlpatterns = [
    path('', webIndex)
]
