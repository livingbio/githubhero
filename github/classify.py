import yaml
import sklearn.externals
import sklearn.preprocessing
import sklearn.ensemble

class RoleClassify(object):
    # define all event and the standard order of events
    cols = [
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

    def __init__(self):
        self.model = sklearn.ensemble.RandomForestRegressor()

    def preprocessing(self, X):
        fill_cols = [col for col in self.cols if col not in X.columns.values]

        for col in fill_cols:
            X[col] = numpy.zeros(len(X))

        # reorder the events
        X = X[self.cols]

        Y = sklearn.preprocessing.normalize(X)
        return Y

    def fit(self, X, Y):
        X = self.preprocessing(X)
        self.model.fit(X, Y)

    def predict(X):
        X = self.preprocessing(X)
        return self.model.predict(X)
