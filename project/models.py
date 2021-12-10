from django.db import models
from datetime import date

class User(models.Model):
    empid = models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    login_time = models.TimeField()
    logout_time = models.TimeField()
    break_hours = models.TimeField()
    remarks = models.CharField(max_length=50)
    
    def __str__(self):
        return self.empid