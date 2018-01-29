from django.urls import path

from . import views

app_name = "test_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:message_id>/vote/', views.vote, name='vote')
]