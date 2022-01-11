from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from erp_attendance.models import AttendanceSheet, Employee
# from django.core.urlresolvers import reverse
from django.urls import reverse


def adminPanel(request):
    # Get employees from db
    employees = Employee.objects.all()
    # for employee in employees:
    #     print('group: ', employee.groups.all.0)
    return render(request, 'adminPanel.html', {'employees': employees})


def showLogin(request):
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

    return HttpResponseRedirect(reverse('adminPanel'))


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
    return HttpResponseRedirect(reverse('adminPanel'))


def deleteEmployee(request, id):
    emp = Employee.objects.get(pk=id)
    emp.user.delete()
    emp.delete()
    return HttpResponseRedirect(reverse('adminPanel'))

def showEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    attendanceSheet = AttendanceSheet.objects.filter(employee=employee)
    print('---------------------------------------------------------------------attendanceSheet: ', attendanceSheet)
    return render(request, 'employeePanel.html', {'employee': employee, 'attendanceSheet': attendanceSheet})

def loginUser(request):
    #logout(request)
    print('login')
    username = password = ''
    if request.POST:
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password=password)
        if user is not None:
            print('user not none')
            if user.is_active:
                print('user is active')
                login(request,user)
                employee = Employee.objects.get(user=user)
                if user.is_superuser:
                    print('is super user')
                    # User is admin
                    # return render(request, 'adminPanel.html', {'employees': employees})
                    # return redirect('admin-panel/', id=yemployee.id)
                    return HttpResponseRedirect(reverse('adminPanel'))
                else:
                    print('is not admin')
                    # User is not admin
                    # return render(request, 'employeePanel.html', {'employee': employee})
                    # return redirect('show-employee/' + employee.id)
                    # return HttpResponseRedirect(reverse('showEmployee', kwargs={id: employee.id}))
                    return HttpResponseRedirect(reverse('showEmployee', args=(employee.id,)))
                    # return HttpResponseRedirect('/accounts/private_profile/%d/'%employee.id)
    return render(request, 'login.html')

def logoutUser(request):
    pass

def addAttendance(request,id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        date = request.POST['date']
        login_time = request.POST['login_time']
        logout_time = request.POST['logout_time']
        break_hours= request.POST['break_hours']
        remarks = request.POST['remarks']
        ins = AttendanceSheet(employee=employee, date=date, login_time=login_time, logout_time=logout_time, break_hours=break_hours, remarks=remarks)
        ins.save()
    return HttpResponseRedirect(reverse('showEmployee', args=(employee.id,)))
    # return redirect('show-employee/' + employee.id)
    # return render(request, 'employeePanel.html',{'employee':employee, 'attendanceSheet': attendanceSheet})