from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="task_index"),
    path('show/', views.show_tasks, name='show_tasks'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
     path('details/<int:task_id>/', views.task_details, name='task_details'),
    path('save_completed_status/<int:task_id>/', views.save_completed_status, name='save_completed_status'),
]
