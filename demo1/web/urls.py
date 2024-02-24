from django.urls import path
from web.views import htmlPage,aboutPage


app_name = "web"

urlpatterns = [
    path('', htmlPage,name="home"),
    path('about-us', aboutPage,name="about")
]
