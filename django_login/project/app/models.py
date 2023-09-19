from django.db import models
# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Firstname
    
    # Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField()
    stu_city = models.CharField(max_length=50)
    class Meta:
        db_table = 'stu_table'
        verbose_name_plural = "Student" 
    
    def _str_(self):
        return self.stu_name
    
class Teacher(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField()
    stu_city = models.CharField(max_length=50)
    class Meta:
        db_table = 'tec_table'
        verbose_name_plural = "Teacher" 
    
    def _str_(self):
        return self.stu_name