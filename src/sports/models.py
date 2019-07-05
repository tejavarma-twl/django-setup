from django.db import models

# Create your models here.
class Sports(models.Model):
    sport_name          = models.TextField()
    Sport_description   = models.TextField()