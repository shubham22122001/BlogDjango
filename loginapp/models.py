from fnmatch import fnmatchcase
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class reg():
    fname = models.CharField()
    lname = models.CharField()
    uname = models.CharField()
    email = models.CharField()
    password = models.CharField()
    address = models.CharField()

class User(AbstractUser):
    is_doctor= models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
