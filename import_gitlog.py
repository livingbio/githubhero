import csv
import os
from github.models import *
import logging

def input(file):
    with open(file) as ifile:
        reader = csv.DictReader(ifile)
        for row in reader:
            row = {
                'repo': row['repository_name'],
                'actor': row['actor'],
                'event': row['type'],
                'count': row['f0_']
            }
            try:
                EventCount(**row).save()
            except Exception as e:
                logging.exception(e)


for i in os.listdir('./git-log'):
    input('./git-log/' + i)
