from django.shortcuts import render
from .models import *
import sklearn.preprocessing
# Create your views here.

class Predictor(object):
    def predict(self, fs):
        return 0

predictors = {
    "master": Predictor(),
    "issue": Predictor(), # issue event
    "coder": Predictor(),
    "document": Predictor(),
    "viewer": Predictor()
}

index = [
    "CommitCommentEvent",
    "CreateEvent",
    "DeleteEvent",
    "DownloadEvent",
    "ForkApplyEvent",
    "ForkEvent",
    "GollumEvent",
    "IssueCommentEvent",
    "IssuesEvent",
    "MemberEvent",
    "PublicEvent",
    "PullRequestEvent",
    "PullRequestReviewCommentEvent",
    "PushEvent",
    "ReleaseEvent",
    "TeamAddEvent",
    "WatchEvent"
]

def contribution(request):
    repo = request.GET.get('repo')

    values = EventCount.fetch(repo)

    names = list(set(k['actor'] for k in values))
    matrix = numpy.zeros((len(names), len(index)))

    for v in values:
        x = names.index(v['actor'])
        y = index.index(v['type'])
        matrix[x,y] = v['f0_']

    matrix = sklearn.preprocessing.normalize(matrix)

    for predict in predictors:
        predict.predict()
