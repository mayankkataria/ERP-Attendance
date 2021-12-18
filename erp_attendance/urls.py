from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.addEmployee, name='addEmployee'),
    path('edit-employee/<int:id>', views.editEmployee, name='editEmployee'),
    path('delete-employee/<int:id>', views.deleteEmployee, name='deleteEmployee'),
]
