from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')


class Department(models.Model):
    department = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name = 'studentid', on_delete= models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField()
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'


    

