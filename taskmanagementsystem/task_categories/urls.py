from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_categories, name="home_categories"),
    path('add_category/', views.add_category, name="add_category"),
    path('edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete/<int:category_id>/', views.delete_category, name='delete_category'),
   
]
