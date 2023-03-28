import json
import csv


def count_issues():
    issues_number = {
    }

    with open('./data/downloaded_data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
        for item in json_data:
            if item['area'] < 10:
                if item['domain'] not in issues_number.keys():
                    issues_number[item['domain']] = {}
                    issues_number[item['domain']]['wrong area size'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                if "wrong area size" not in issues_number[item['domain']].keys():
                    issues_number[item['domain']]['wrong area size'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                else:
                    issues_number[item['domain']]['wrong area size']['ads'].extend([item['rentola'], item['source']])
                    issues_number[item['domain']]['wrong area size']['ads_num'] += 1

            if item['images_length'] == 1:
                if item['domain'] not in issues_number.keys():
                    issues_number[item['domain']] = {}
                    issues_number[item['domain']]['wrong_img_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                elif "wrong_img_num" not in issues_number[item['domain']].keys():
                    issues_number[item['domain']]['wrong_img_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                else:
                    issues_number[item['domain']]['wrong_img_num']['ads'].extend([item['rentola'], item['source']])
                    issues_number[item['domain']]['wrong_img_num']['ads_num'] += 1

            if not item['bathrooms'] or 20 < item['bathrooms'] == 0:
                if item['domain'] not in issues_number.keys():
                    issues_number[item['domain']] = {}
                    issues_number[item['domain']]['wrong_bathrooms_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                elif "wrong_bathrooms_num" not in issues_number[item['domain']].keys():
                    issues_number[item['domain']]['wrong_bathrooms_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                else:
                    issues_number[item['domain']]['wrong_bathrooms_num']['ads'].extend(
                        [item['rentola'], item['source']])
                    issues_number[item['domain']]['wrong_bathrooms_num']['ads_num'] += 1

            if not item['bedrooms'] or 20 < item['bedrooms'] == 0:
                if item['domain'] not in issues_number.keys():
                    issues_number[item['domain']] = {}
                    issues_number[item['domain']]['wrong_bedrooms_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                elif "wrong_bedrooms_num" not in issues_number[item['domain']].keys():
                    issues_number[item['domain']]['wrong_bedrooms_num'] = {
                        "ads": [item['rentola'], item['source']],
                        "ads_num": 1,
                    }
                else:
                    issues_number[item['domain']]['wrong_bedrooms_num']['ads'].extend([item['rentola'], item['source']])
                    issues_number[item['domain']]['wrong_bedrooms_num']['ads_num'] += 1

    return issues_number


def summary(issue_data):
    fields = ['domain', 'wrong area size', 'wrong_img_num', 'wrong_bathrooms_num',
              'wrong_bedrooms_num']
    with open("./data/summary.csv", "w+") as out_file:
        write = csv.writer(out_file)
        write.writerow(fields)
        for domain, issue in issue_data.items():
            write.writerow([domain, issue.get('wrong area size', {}).get('ads_num', 0),
                            issue.get('wrong_img_num', {}).get('ads_num', 0),
                            issue.get('wrong_bathrooms_num', {}).get('ads_num', 0),
                            issue.get('wrong_bedrooms_num', {}).get('ads_num', 0)])


# wrong area size wrong_img_num wrong_bathrooms_num wrong_bedrooms_num
if __name__ == "__main__":
    issues = count_issues()
    summary(issues)

    with open("../data/JIRA/jira_tickets.csv", "w+") as out_file:
        write = csv.writer(out_file)
        write.writerow(['title', 'description'])

        for domain, values in issues.items():
            description = ''
            title = f"[{domain}]"
            if values.get('wrong_bathrooms_num', {}).get('ads_num', 0):
                description += "WRONG BATHROOM NUM\n{}\n".format(
                    '\n'.join(values.get('wrong_bathrooms_num', {}).get('ads')[:2]))

            if values.get('wrong_img_num', {}).get('ads_num', 0):
                description += "WRONG IMAGES NUM\n{}\n".format('\n'.join(values.get('wrong_img_num', {}).get('ads')[:2]))

            if values.get('wrong area size', {}).get('ads_num', 0):
                description += "WRONG  AREA VALUE\n{}\n".format('\n'.join(values.get('wrong area size', {}).get('ads')[:2]))

            write.writerow([title, description])
