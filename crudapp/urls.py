from django.urls import path

from . import views

app_name = "crudapp"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new', views.post_create, name='post_new'),
    path('edit/<int:pk>/', views.post_update, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('emp', views.emp, name='emp_create'),
    path('show', views.show, name='emp_show'),
    path('edit/<int:id>', views.edit, name='emp_edit'),
    path('update/<int:id>', views.update, name='emp_update'),
    path('delete/<int:id>', views.destroy, name='emp_delete'),
]
