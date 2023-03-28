import scrapy
import re
import csv
import pandas as pd


class ReadingLogsSpider(scrapy.Spider):
    name = 'reading_logs'
    allowed_domains = ['scrapyd.rentola.tech']
    start_urls = ['http://scrapyd.rentola.tech/']

    def start_requests(self):
        yield scrapy.Request("https://fbadmin:adminfb@scrapyd.rentola.tech/0/jobs", meta={"playwright": True})

    def parse(self, response, **kwargs):
        for row in response.xpath('//table//tr'):
            columns = row.xpath('./td')
            if len(columns) == 9 and row.xpath('./td[7]/text()').get():
                spider_name = row.xpath('./td[2]/text()').get()
                running_time = row.xpath('./td[6]/text()').get()
                log_link = row.xpath('./td[8]//@href').get()
                yield scrapy.Request(f"https://scrapyd.rentola.tech{log_link}", meta={
                    "playwright": True,
                    "spider_name": spider_name,
                    "running_time": running_time,
                },

                                     callback=self.reading_logs)

    def reading_logs(self, response, **kwargs):
        logs = response.xpath('//pre/text()').get()
        returned_errors = error_search(logs)
        spider_name = response.meta['spider_name']
        running_time = response.meta['running_time']

        if returned_errors:
            yield {
                "spider_name": spider_name,
                "running_time": running_time,
                "No of Errors": len(returned_errors),
                "ERROR": [*returned_errors][0],
                "log_link": response.url,
            }


def error_search(log_file):
    returned_errors = []
    error_patterns = ['ERROR: Spider error processing', 'ERROR: Gave up retrying', 'UnboundLocalError',
                      'ValueError:', 'IndexError:', 'TypeError:', 'TimeoutError', 'ERROR: Error downloading']

    for log in log_file.splitlines():
        for error_pattern in error_patterns:
            if re.search(error_pattern, log):
                returned_errors.append(log)
    return set(returned_errors)
