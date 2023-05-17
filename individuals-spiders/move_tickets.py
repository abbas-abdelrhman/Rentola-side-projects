import json

import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("e-mail",
                     "auth-code")


def add_comment(issueIdOrKey, comment, log_link):
    url = f"https://rentola.atlassian.net/rest/api/3/issue/{issueIdOrKey}/comment"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "body": {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": f"{comment} | ",
                            "type": "text"
                        },
                        {
                            "type": "text",
                            "text": "Log link",
                            "marks": [
                                {
                                    "type": "link",
                                    "attrs": {
                                        "href": f"{log_link}"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    })

    requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )


def moving_tickets(issueIdOrKey, column_id):
    url = f"https://rentola.atlassian.net/rest/api/3/issue/{issueIdOrKey}/transitions"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps(
        {
            "transition": {
                "id": f"{column_id}"
            }
        }
    )

    requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )


if __name__ == '__main__':
    with open('/home/abbas/PycharmProjects/individuals-spiders/individuals_spiders/test.json', 'r') as file:
        tickets = json.loads(file.read())
        for ticket in tickets:
            if ticket.get("No of Errors", 0) == 1:
                moving_tickets(ticket.get('_id'), '31')
                print(ticket.get('issue_link'), ticket.get('scraped_items'))

                # add_comment(ticket.get('_id'),
                #             f"please, check the log file to see if it is possible to solve the errors.",
                #             ticket.get('log_link'))
                # moving_tickets(ticket.get('_id'), '41')

            elif ticket.get("No of Errors", 0) > 1:
                add_comment(ticket.get('_id'),
                            f"please, check the log file and solve the errors.",
                            ticket.get('log_link'))
                moving_tickets(ticket.get('_id'), '41')

            if ticket.get("No of Errors", 0) == 0:
                moving_tickets(ticket.get('_id'), '31')
                print(ticket.get('issue_link'), ticket.get('scraped_items'))
