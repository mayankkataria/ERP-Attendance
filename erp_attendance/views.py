from django.contrib.auth.models import User
from django.shortcuts import render

from erp_attendance.models import Employee

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
