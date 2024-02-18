from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')