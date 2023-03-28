# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import csv

import requests
from requests.auth import HTTPBasicAuth
import json

auth = HTTPBasicAuth("abdelrahmanabbas@rentola.com",
                     "ATATT3xFfGF0DfHikWVALUl1pUOseFl9GHHFHB99T5mZYvDiBErDESLVdechg4giVAT09ZBN9lVtsC2tUQb8AKns5RhYgKy_nJnjSUaVx01HmWdtjHYFyjANP75k3Yj5-s_OQTedNtSCajRhBwUp2VlbzPB9DbyRRv2XEjzWXHQ1-Fh3JzZo3Jk=D7F14C08")


def main(title, description):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project":
                {
                    "key": "SFR"
                },
            "summary": title,
            "description": description,
            "issuetype": {
                "name": "Task"
            }
        }
    })

    response = requests.request(
        "POST",
        "https://rentola-dev.atlassian.net/rest/api/2/issue/",
        data=payload,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def gen_tickets():
    with open('data/JIRA/jira_tickets.csv', "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            main(row[0],row[1])

if __name__ == '__main__':
    pass
    # gen_tickets()