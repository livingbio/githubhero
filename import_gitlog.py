import sys, os
sys.path.append('./githubhero')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import csv
from github.models import *
import logging


def input(file):
    with open(file) as ifile:
        reader = csv.DictReader(ifile)
        for row in reader:
            repo, _ = Repository.objects.get_or_create(name = row['repository_name'])
            actor, _ = User.objects.get_or_create(name=row['actor'])
            event, _ = Event.objects.get_or_create(name=row['type'])

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


for i in os.listdir('./git-log'):
    print 'process', i
    input('./git-log/' + i)
