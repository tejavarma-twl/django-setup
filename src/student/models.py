from django.db import models

# Create your models here.
class Student(models.Model):
    name    = models.TextField()
    branch  = models.TextField()
    year    = models.TextField()
    phone    = models.TextField()
