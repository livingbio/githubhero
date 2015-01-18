from django.db import models
from jsonfield import JSONField


class Repository(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)

class Event(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class EventCount(models.Model):
    repo = models.ForeignKey(Repository)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    count = models.IntegerField()

    class Meta:
        unique_together = ((repo, user, event), )

class Role(models.Model):
    repo = models.ForeignKey(Repository)
    user = models.ForeignKey(User)

    contributions = JSONField(default="{}")

    class Meta:
        unique_together = ((repo, user), )
