from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=120)
    pwd   = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    city  = models.CharField(max_length=120)
    address=models.CharField(max_length=120)