from django.db import models

class Resume(models.Model):
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')