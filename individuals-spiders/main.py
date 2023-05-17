# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import csv

import requests
from requests.auth import HTTPBasicAuth
import json



def jira_tickets():
    auth = HTTPBasicAuth("email",
                         "auth-code")

    url = """https://rentola-dev.atlassian.net/rest/api/3/search?jql=project%20%3D%20"SFR"%20AND%20status%20%3D%20"Waiting%204%20Automatic%20Submission"%20AND%20updated%20<%3D%20-1w%20ORDER%20BY%20assignee%20ASC%2C%20created%20DESC%2C%20issuekey%20ASC%2C%20summary%20ASC&referrer=agility&maxResults=100"""

    tickets = {}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request(
        method="GET",
        url=url,
        headers=headers,
        auth=auth
    )

    for issue in json.loads(response.text).get('issues'):
        tickets[f"https://rentola.atlassian.net/browse/{issue.get('key')}"] = issue.get('fields').get('summary')

    return tickets


if __name__ == '__main__':
    with open('jira_tickets.json','w+') as file:
        file.write(json.dumps(jira_tickets()))


