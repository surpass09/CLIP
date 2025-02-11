from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class OutlookUserData(models.Model):
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    events = ArrayField(models.CharField(max_length=200), size=40)
    timings = models.DateTimeField()







