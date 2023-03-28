import json
import csv


def formatiing_data():
    formatiing_json = {}

    with open('./data/downloaded_data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
        for item in json_data:
            if item['domain'] in formatiing_json:

                if item['source'] not in formatiing_json[item['domain']]:
                    formatiing_json[item['domain']].extend(
                        (item['rentola'], item['source'], item['bedrooms'], item['bathrooms'], item['area']))

            else:
                formatiing_json[item['domain']] = [

                    item['rentola'],
                    item['source'],
                    item['bedrooms'],
                    item['bathrooms'],
                    item['area']

                ]

    with open('./data/formatiing_data.json', 'w+') as file:
        file.write(json.dumps(formatiing_json))

    return formatiing_json


# def presenting_data(data_sheet1):
#     jira_tickets = {}
#     with open('data/spidernest_data.json', 'r') as spdidernest_data:
#         data = json.loads(spdidernest_data.read())
#         for item1 in data:
#             for key, value in item1.items():
#                 domain = key
#                 dev_name = value['dev_name']
#                 records = value['records']
#                 external_source = value['name']
#
#                 edit_ex_src = None
#                 if external_source != value['filled_external_source']:
#                     edit_ex_src = "Update the external_source on spider nest".upper()
#
#                 title = f"[{domain}] Wrong price value | {external_source}"
#                 issue_links = "\n".join(data_sheet1[domain])
#                 if edit_ex_src:
#                     description = f"""{edit_ex_src}\n{issue_links}\nNo of records {records}\nSpider created by {dev_name}"""
#                 else:
#                     description = f"""{issue_links}\nNo of records {records}\nSpider created by {dev_name}"""
#
#                 jira_tickets[title] = description.strip()
#
#     with open('data/jira_tickets.csv', "w+") as jira_file:
#         writer = csv.writer(jira_file)
#         writer.writerow(["title", "description"])
#         for key, value in jira_tickets.items():
#             writer.writerow([key, value])


if __name__ == "__main__":
    formatiing_data()
