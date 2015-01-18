from django.db import models

# Create your models here.

class EventCount(models.Model):
    repo = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    count = models.IntegerField()



