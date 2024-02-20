from django.urls import path
from web.views import webIndex,htmlPage,aboutPage


urlpatterns = [
    path('', webIndex),
    path('web/', htmlPage),
    path('web/about', aboutPage)
]
