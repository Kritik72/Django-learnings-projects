from django.db import models

class Student(models.Model):

    # id = models.AutoField()
    name = models.CharField(max_length = 25)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    phoneNumber = models.TextField(null=True)

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default = 50)

class professor(models.Model):
    prof_name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 25)
    age = models.IntegerField()
    

    