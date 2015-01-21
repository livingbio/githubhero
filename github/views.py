from django.shortcuts import render
from .models import *
from .classify import *
import sklearn.preprocessing
import pandas
# Create your views here.

def contribution(request):
    repo = request.GET.get('repo')

    values = EventCount.fetch(repo)
    X = numpy.zeros(
        (len(values), ),
        dtype=[
            ('name', 'a10'),
            ('event', 'a30'),
            ('count', 'i4')
        ])
    X[:] = values
    X = DataFrame(X)

    X = pandas.tools.pivot.pivot_table(
        X,
        value='count',
        index=['name'],
        columns=['event'],
        fill_value=0
    )


