from django.urls import path
from parser_site import views

app_name = "parser_site"
urlpatterns = [
    path('index', views.index),
    path('parse', views.main_func),
]