from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, error_messages={'required':'Enter your name'}) # _ converted into space and first charector converted into Uppercase
    email = models.EmailField()
    phone = models.CharField(max_length=200)
