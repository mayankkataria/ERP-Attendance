from django.contrib import admin

from erp_attendance.models import AttendanceSheet, Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(AttendanceSheet)