from django.db import models
from jsonfield import JSONField
from .service_provider import *

class Repository(models.Model):
    name = models.CharField(max_length=255, unique=True)

class User(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)

# Create your models here.
class EventCount(models.Model):
    repo = models.ForeignKey(Repository)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    count = models.IntegerField()

    class Meta:
        unique_together = (('repo', 'user', 'event'), )

    @classmethod
    def fetch(cls, repo):
        query = "SELECT actor, type, f0_ FROM [github.githubhero] WHERE repository_name = '%s'" % repo
        results, num = execute(734869178378, query)
        return results

class Role(models.Model):
    repo = models.ForeignKey(Repository)
    user = models.ForeignKey(User)

    contributions = JSONField(default="{}")

    class Meta:
        unique_together = (('repo', 'user'), )
