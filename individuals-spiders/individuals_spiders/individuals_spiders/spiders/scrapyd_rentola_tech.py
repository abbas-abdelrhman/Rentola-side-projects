import scrapy
import re
import requests
from requests.auth import HTTPBasicAuth
import json

log_date = "2023-03-27"


class ScrapydRentolaTechSpider(scrapy.Spider):
    name = "scrapyd_rentola_tech"
    allowed_domains = ["scrapyd.rentola.tech"]
    start_urls = [
        "https://scrapyd.rentola.tech/0/logs/python_spiders/",
        "https://scrapyd.rentola.tech/1/logs/python_spiders/",
        "https://scrapyd.rentola.tech/2/logs/python_spiders/",
        "https://scrapyd.rentola.tech/3/logs/python_spiders/"
    ]

    headers = {
        "authorization": "Basic auth-code",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,
                                 headers=self.headers,
                                 callback=self.parse,
                                 )

    def parse(self, response, **kwargs):
        for issue_link, s_name in jira_tickets().items():
            if response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{s_name[0]}')]/@href").get():
                log_link_pg = response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{s_name[0]}')]/@href").get()
                scrapyd = f"{response.url}{log_link_pg}"
                yield scrapy.Request(url=scrapyd,
                                     headers=self.headers,
                                     callback=self.parse_2,
                                     meta={
                                         "spider_name": s_name[0],
                                         "issue_link": issue_link,
                                         "_id": s_name[1]
                                     }
                                     )

            elif response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{rm(s_name[0])}')]/@href").get():
                log_link_pg = response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{rm(s_name[0])}')]/@href").get()
                scrapyd = f"{response.url}{log_link_pg}"
                yield scrapy.Request(url=scrapyd,
                                     headers=self.headers,
                                     callback=self.parse_2,
                                     meta={
                                         "spider_name": s_name[0],
                                         "issue_link": issue_link,
                                         "_id": s_name[1]
                                     }
                                     )
            elif response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{rm(rm(s_name[0]))}')]/@href").get():
                log_link_pg = response.xpath(
                    f"//td/a[contains(translate(.,   'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{rm(rm(s_name[0]))}')]/@href").get()
                scrapyd = f"{response.url}{log_link_pg}"
                yield scrapy.Request(url=scrapyd,
                                     headers=self.headers,
                                     callback=self.parse_2,
                                     meta={
                                         "spider_name": s_name[0],
                                         "issue_link": issue_link,
                                         "_id": s_name[1]
                                     }
                                     )

    def parse_2(self, response):
        logs = response.xpath('//td/a/@href').getall()
        for log in logs:
            log_link = f"{response.url}{log}"
            body = requests.get(log_link, headers=self.headers)
            if body.text.split('[')[0].split(' ')[0] == log_date:
                yield scrapy.Request(url=log_link,
                                     headers=self.headers,
                                     callback=self.reading_logs,
                                     meta={
                                         "spider_name": response.meta["spider_name"],
                                         "issue_link": response.meta['issue_link'],
                                         '_id': response.meta['_id']
                                     }
                                     )

    def reading_logs(self, response, **kwargs):
        error_patterns = ['ERROR: Spider error processing', 'JSONDecodeError','ERROR: Gave up retrying', 'UnboundLocalError',
                          'ValueError:', 'IndexError:', 'TypeError:', 'TimeoutError', 'ERROR: Error downloading']
        error_found = []
        body = response.text
        for error in error_patterns:
            if re.findall(error, body):
                error_found.extend(re.findall(error, body))

        scraped_items = re.findall("item_scraped_count': (\d+)", body)
        if scraped_items:
            scraped_items = scraped_items[0]
        else:
            scraped_items = 0

        yield {
            "spider_name": response.meta["spider_name"],
            "No of Errors": len(set(error_found)),
            "ERROR": set(error_found),
            "scraped_items": scraped_items,
            '_id': response.meta['_id'],
            "log_link": response.url,
            "issue_link": response.meta['issue_link'],

        }


def jira_tickets():
    auth = HTTPBasicAuth("email",
                         "auth-code")

    # url = """https://rentola-dev.atlassian.net/rest/api/3/search?jql=project%20%3D%20"SFR"%20AND%20status%20%3D%20"Waiting%204%20Automatic%20Submission"%20AND%20updated%20<%3D%20-1w%20ORDER%20BY%20assignee%20ASC%2C%20created%20DESC%2C%20issuekey%20ASC%2C%20summary%20ASC&referrer=agility&maxResults=100"""
    url = """https://rentola-dev.atlassian.net/rest/api/3/search?jql=project%20%3D%20"SFR"%20AND%20status%20IN%20%28"Waiting%204%20Automatic%20Submission"%29%20AND%20assignee%20%3D%20"61e56a235fcc370068593255"%20ORDER%20BY%20created%20DESC%2C%20issuekey%20ASC%2C%20summary%20ASC&referrer=agility"""
    s_names = {}
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
        _id = issue.get('id')
        if "_pyspider_" in issue.get('fields').get('summary'):
            s_name = re.findall("([\w]+)_PySpider_", issue.get('fields').get('summary'))[0]
            s_names[f"https://rentola-dev.atlassian.net/browse/{issue.get('key')}"] = s_name, _id
        else:
            s_name = issue.get('fields').get('summary').split(' ')[0]
            s_names[f"https://rentola-dev.atlassian.net/browse/{issue.get('key')}"] = clean(s_name), _id

    # return s_names
    return {'https://rentola.atlassian.net/browse/SFR-2182': ('alphabitat', 'SFR-2182'),
            # 'https://rentola-dev.atlassian.net/browse/SFR-218': ('ladresse.com', 'SFR-2182'),
            }


def clean(text):
    if "https://" or "http://" in text:
        text = text.split('//')[-1]

    chars = ['.', '-']
    for char in chars:
        text = text.replace(char, '_')

    chars2 = ['[', ']', '/']
    for char in chars2:
        text = text.replace(char, '')
    return text


def rm(text):
    nw_text = "_".join(text.split('_')[:-1])
    return nw_text

