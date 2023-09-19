from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    age=models.IntegerField()
    image=models.FileField (upload_to='myimages')
