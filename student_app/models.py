from django.db import models

# Create your models here.
class complaintdetailss(models.Model):
    userid = models.CharField(max_length=50)
    complaintto = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    complaintmsg = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
   