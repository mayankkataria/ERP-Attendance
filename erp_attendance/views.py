from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from erp_attendance.models import Employee

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def addEmployee(request):
    print('----------------------------------add employee-----------------------------------------')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    empid = request.POST['empid']
    email = request.POST['email']
    department = request.POST['department']
    isAdmin = request.POST.get('isAdmin') == 'on'
    print('-------------------------------------isAdmin-----------------------------------------', isAdmin)
    user = User.objects.create_user(username, email, 'Arcgate1!')
    user.is_superuser = isAdmin
    user.first_name = firstname
    user.last_name = lastname
    user.save()

    employee = Employee(user=user, empid=empid)
    employee.save()

    group = Group.objects.get(name=department)
    group.user_set.add(user)

    return HttpResponseRedirect('/')