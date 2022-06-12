# from fnmatch import fnmatchcase
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

class blog_data2(models.Model):
    userName=models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    summary=models.TextField(max_length=255)
    content=models.TextField(max_length=255)
    status=models.CharField(max_length=255)
    # image = models.ImageField(upload_to='uploads/')
    # image= models.FileField(upload_to='images/', null=True, verbose_name="")




    def __str__(self):
        return self.title + " by " + self.username