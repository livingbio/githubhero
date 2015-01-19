from oauth2client import gce
import httplib2
from apiclient.discovery import build

def service(service, version, scope):
    credentials = gce.AppAssertionCredentials(scope=scope)
    http = credentials.authorize(httplib2.Http())
    return build(service, version, http=http)
    

def bigquery():
    return service('bigquery', 'v2', 'https://www.googleapis.com/auth/devstorage.read_write')

def execute(bqproject, query):
    service = bigquery()
    jobs = service.jobs()

    results = jobs.query(
        projectId=bqproject,
        body={
            'query': query,
            "useQueryCache": True
        }
    ).execute()

    schema = [] 
    for field in results['schema']['fields']:
        if field['type'] == "STRING":
            schema.append(str)
        elif field['type'] == "INTEGER":
            schema.append(int)

    if 'rows' in results:
        data = [[s(v['v']) for s, v in zip(schema, row['f'])] for row in results['rows']]
        num = int(results.get('totalRows'))

        return data, num
    else:
        return [], 0


if __name__ == "__main__":
    print execute(734869178378, "SELECT actor, type, f0_ FROM [github.githubhero] where repository_name = 'gcloud-python'")
