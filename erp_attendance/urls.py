from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.showLogin, name='showLogin'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    # path('admin-panel/<int:id>', views.adminPanel, name='adminPanel'),
    path('admin-panel/', views.adminPanel, name='adminPanel'),
    path('add-employee/', views.addEmployee, name='addEmployee'),
    path('edit-employee/<int:id>', views.editEmployee, name='editEmployee'),
    path('delete-employee/<int:id>', views.deleteEmployee, name='deleteEmployee'),
    path('show-employee/<int:id>', views.showEmployee, name='showEmployee'),
    path('attendance-sheet/<int:id>', views.addAttendance, name='addAttendance'),
    path('add-attendance/<int:id>',views.addAttendance, name = 'addAttendance'),
]
