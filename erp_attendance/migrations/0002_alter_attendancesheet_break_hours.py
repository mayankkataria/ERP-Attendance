# Generated by Django 3.2.9 on 2021-12-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancesheet',
            name='break_hours',
            field=models.IntegerField(max_length=2),
        ),
    ]
