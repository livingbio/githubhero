import sys, os
sys.path.append('./githubhero')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import csv
from github.models import *
import logging

repos = {}
users = {}
events = {}

def input(file):
    with open(file) as ifile:
        reader = csv.DictReader(ifile)
        for row in reader:
            repo = row['repository_name']
            actor = row['actor']
            type = row['type']
            if not repo or not actor or not type: continue
            if len(repos) > 1000000:
                repos.clear()
            if len(users) > 1000000:
                users.clear()

            repo = repos.setdefault(repo, Repository.objects.get_or_create(name = repo)[0])
            actor = users.setdefault(actor, User.objects.get_or_create(name=actor)[0])
            event = events.setdefault(type, Event.objects.get_or_create(name=type)[0])

            row = {
                'repo': repo,
                'user': actor,
                'event': event,
                'count': row['f0_']
            }

            try:
                EventCount.objects.create(**row)
            except Exception as e:
                logging.exception(e)


for i in reversed(os.listdir('./git-log')):
    print 'process', i
    input('./git-log/' + i)
