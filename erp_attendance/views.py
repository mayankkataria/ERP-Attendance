from datetime import datetime
from django import template
from django.contrib.auth.models import Group, User
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from erp_attendance.models import AttendanceSheet, Employee
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.core import serializers

def adminPanel(request):
    # Get employees from db
    employees = Employee.objects.all()

    # Field admins with sessions
    kpoAdmins = serializers.serialize('json', User.objects.filter(is_superuser=True, groups__name='KPO'))
    softwareAdmins = serializers.serialize('json', User.objects.filter(is_superuser=True, groups__name='Software'))
    onlyUsers = serializers.serialize('json', User.objects.filter(is_superuser=False))
    request.session['kpo_admins'] = kpoAdmins
    request.session['software_admins'] = softwareAdmins
    request.session['only_users'] = onlyUsers

    # Cookies showing total days of visits
    visits = int(request.COOKIES.get('visits', '0'))

    response = HttpResponse(render(request, 'adminPanel.html', {'employees': employees}))

    # if request.COOKIES.has_key('last_visit'):
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        # the cookie is a string - convert back to a datetime type
        last_visit_time = datetime.strptime(
            last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        curr_time = datetime.now()
        if (curr_time-last_visit_time).days > 0:
            # if at least one day has gone by then inc the visit count.
            response.set_cookie('visits', visits + 1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response.set_cookie('last_visit', datetime.now())

    # if request.COOKIES.has_key( 'visits' ):
    if 'visits' in request.COOKIES:
            v = request.COOKIES[ 'visits' ]
    else:
            v = 0

    print('visits: ', v)
    return response
    # return render(request, 'adminPanel.html', {'employees': employees})


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
    print('sessions: KPO_admins: ', request.session['kpo_admins'], '\nSoftware_admins: ', request.session['software_admins'], '\nOnly_users', request.session['only_users'])
    employee = Employee.objects.get(pk=id)
    attendanceSheet = AttendanceSheet.objects.filter(employee=employee)
    return render(request, 'employeePanel.html', {'employee': employee, 'attendanceSheet': attendanceSheet})


def loginUser(request):
    # logout(request)
    print('login')
    username = password = ''
    if request.POST:
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('user not none')
            if user.is_active:
                print('user is active')
                login(request, user)
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


def addAttendance(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        date = request.POST['date']
        login_time = request.POST['login_time']
        logout_time = request.POST['logout_time']
        break_hours = request.POST['break_hours']
        remarks = request.POST['remarks']
        ins = AttendanceSheet(employee=employee, date=date, login_time=login_time,
                              logout_time=logout_time, break_hours=break_hours, remarks=remarks)
        ins.save()
    return HttpResponseRedirect(reverse('showEmployee', args=(employee.id,)))
    # return redirect('show-employee/' + employee.id)
    # return render(request, 'employeePanel.html',{'employee':employee, 'attendanceSheet': attendanceSheet})


def validateForm(request):
    errorField = ''
    if 'username' in request.GET:
        username = request.GET['username']
        usernames = User.objects.filter(username=username)
        if len(usernames) == 1:
            errorField = 'Username'
    elif 'email' in request.GET:
        email = request.GET['email']
        emails = User.objects.filter(email=email)
        if len(emails) == 1:
            errorField = 'Email'
    else:
        empid = request.GET['empid']
        empids = Employee.objects.filter(empid=empid)
        if len(empids) == 1:
            errorField = 'Employee ID'
    if errorField != '':
        return HttpResponse(errorField + ' already exists')
    else:
        return HttpResponse('')


def searchEmployees(request):
    searchedEmp = request.GET['searchedEmp']
    isAdmin = request.GET['isAdminDropdown']
    deptName = request.GET['deptName']
    employees = Employee.objects.filter(user__username=searchedEmp, user__is_superuser = isAdmin, user__groups__name = deptName)
    return render(request, 'adminPanel.html', {'employees': employees})
