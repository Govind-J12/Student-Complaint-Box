from django.db import models

# Create your models here.
class studentdetails(models.Model):
    studentphoto = models.ImageField()
    studentname = models.CharField(max_length=50)
    studentemail = models.CharField(max_length=50)
    studentphone = models.CharField(max_length=50)
    studentpassword = models.CharField(max_length=50)
