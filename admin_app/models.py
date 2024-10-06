from django.db import models

# Create your models here.
class addfaculty(models.Model):
    designation = models.CharField(max_length=50)
    facultyname = models.CharField(max_length=50)
    facultyemail = models.CharField(max_length=50)
    facultypassword = models.CharField(max_length=50)
    
class adminack(models.Model):
    ackdate = models.CharField(max_length=50)
    ackdesignation = models.CharField(max_length=50)
    ackname = models.CharField(max_length=50)
    ackemail = models.CharField(max_length=50)
    ackmsg = models.CharField(max_length=50)
