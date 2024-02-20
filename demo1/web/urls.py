from django.urls import path
from web.views import webIndex,htmlPage,aboutPage


app_name = "web"

urlpatterns = [
    path('', webIndex),
    path('web/', htmlPage,name="home"),
    path('web/about-us', aboutPage,name="about")
]
