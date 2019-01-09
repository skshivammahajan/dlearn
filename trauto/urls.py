from django.urls import path

from . import views

app_name = "trauto"

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.node_list, name='node_list'),
    path('mail', views.mail)
]