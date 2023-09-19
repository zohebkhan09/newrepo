from django.db import models
class AadharModel(models.Model):
    aadhar_no=models.IntegerField()

# Create your models here.
class StudentModel(models.Model):
    stu_name=models.CharField(max_length=100)
    aadhar_no=models.OnetoOneField(AadharModel,
            on_delete=models.CASCADE,primary_key=True)
    def__str__(self):
    return self.stu_name