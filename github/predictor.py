import yaml
from sklearn.externals import joblib

settings = yaml.load(open('conf.yaml').read())
predictors = {}
for p in settings['predictors']:
    predictors[p] = joblib.load(p['uri'])


def predict(vs):
    results = []
    for p in predictors:
        results.append(predictors[p].predict_proba(vs))
