from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from erp_attendance.models import Employee


def index(request):
    # Get employees from db
    employees = Employee.objects.all()
    # for employee in employees:
    #     print('group: ', employee.groups.all.0)
    return render(request, 'index.html', {'employees': employees})


def login(request):
    return render(request, 'login.html')


def addEmployee(request):
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


def editEmployee(request, id):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    empid = request.POST['empid']
    email = request.POST['email']
    department = request.POST['department']
    isAdmin = request.POST.get('isAdmin') == 'on'

    employee = Employee.objects.get(pk=id)
    employee.empid = empid
    employee.save()

    user = employee.user
    user.username = username
    user.email = email
    user.is_superuser = isAdmin
    user.first_name = firstname
    user.last_name = lastname
    user.save()
    group = Group.objects.get(name=department)
    group.user_set.add(user)
    return HttpResponseRedirect('/')


def deleteEmployee(request, id):
    emp = Employee.objects.get(pk=id)
    emp.user.delete()
    emp.delete()
    return HttpResponseRedirect('/')

def showEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    print('employee: ', employee)
    return render(request, 'details.html', {'employee': employee})

