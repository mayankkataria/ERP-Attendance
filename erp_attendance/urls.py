from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.addEmployee, name='addEmployee'),
    path('edit-employee/<int:id>', views.editEmployee, name='editEmployee'),
    path('delete-employee/<int:id>', views.deleteEmployee, name='deleteEmployee'),
    path('show-employee/<int:id>', views.showEmployee, name='showEmployee'),
    path('validate-form/', views.validateForm, name='validateForm')
]
