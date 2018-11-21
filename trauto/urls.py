from django.urls import path

from . import views

app_name = "trauto"

urlpatterns = [
    path('', views.index, name='index'),
]