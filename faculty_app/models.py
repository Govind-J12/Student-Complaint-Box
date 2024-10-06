from django.db import models

# Create your models here.
class stdack(models.Model):
    username = models.CharField(max_length=50)
    userdate = models.CharField(max_length=50)
    useremail = models.CharField(max_length=50)
    userackmsg = models.CharField(max_length=50)
