from xmlrpc.client import Boolean
from django.db import models
from datetime import date
from django.contrib.auth.models import User, Group
from django.db.models.deletion import SET_NULL

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=SET_NULL, null=True)
    empid = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.empid

class AttendanceSheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=SET_NULL, null=True)
    date = models.DateField(default=date.today)
    login_time = models.TimeField()
    logout_time = models.TimeField()
    break_hours = models.IntegerField()
    remarks = models.CharField(max_length=50)