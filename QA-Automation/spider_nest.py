import json

import scrapy

from scrapy.crawler import CrawlerProcess


class SpiderNest(scrapy.Spider):
    name = "spider_nest"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }
    cookies = {
        "_spider_nest_session": 'n7bTUlmD%2Bjyo4aqsL%2BCywD6okrU3wqTsL8dR3d7VQuaMVb5fB%2Bdnj6ajAIBF1cu09aWIoWVvOZEA22hNaMR0x58TQi60AJvY8%2BGVPzChkjIaj1Z5hxf%2FcoE6rTvcN5XxznTuz%2F9CXz%2BKGr0P%2B%2B6M%2BFLQ2%2FPCVM8HIaSwDop6%2BAFyS5vw%2BudjhxfYYXR4Fc1OFYEj1jKAzrojbVobA2iqRs8ed%2BDr8qpfTJBRla%2Bu5XJGdqjeT%2BID0D9%2FRVcEzA%3D%3D--n7S0QhzkljAtcyyp--LV72U8dehNIZdF2F8kMXqQ%3D%3D',
    }

    # 1. SCRAPING level 1
    def start_requests(self):
        with open('data/formatiing_data.json', "r") as domain_file:
            domains = json.loads(domain_file.read()).keys()
            for domain in domains:
                yield scrapy.Request(url=f"https://c.findboliger.dk/spider_details?spider_detail%5Bdomain%5D={domain}",
                                     headers=self.headers,
                                     cookies=self.cookies,
                                     callback=self.parse,
                                     meta={'domain': domain}
                                     )

    # 2. SCRAPING level 2
    def parse(self, response, **kwargs):

        for item in response.xpath('//table[@class="table"]/tbody//tr'):
            dev_name = item.xpath('./td[11]//text()').get()
            submission_link = item.xpath('.//a[@title="View Submissions"]/@href').get()
            edit_link = item.xpath('.//a[@title="Edit"]/@href').get()

            if submission_link:
                yield scrapy.Request(
                    url="https://c.findboliger.dk{}".format(edit_link),
                    callback=self.edit_page,
                    cookies=self.cookies,
                    headers=self.headers,
                    meta={
                        'submission_link': submission_link,
                        "dev_name": dev_name,
                        "domain": response.meta['domain']
                    }
                )

    def edit_page(self, response):
        dev_name = response.meta['dev_name']
        submission_link = response.meta['submission_link']

        filled_external_source = response.xpath('//input[@id="spider_detail_name"]/@value').get()

        yield scrapy.Request(
            url="https://c.findboliger.dk{}".format(submission_link),
            callback=self.submission_page,
            cookies=self.cookies,
            headers=self.headers,
            meta={
                "dev_name": dev_name,
                "filled_external_source": filled_external_source,
                "domain": response.meta['domain']

            }
        )

    def submission_page(self, response):

        records = country = name = sub_status = None
        for item in response.xpath('//table[@class="table"]//tr'):
            sub_status = item.xpath('./td[1]/i/@title').get()
            name = item.xpath('./td[1]/a/text()').get()
            country = item.xpath('./td[3]//text()').get()
            records = item.xpath('./td[5]//text()').get()

        yield {
            response.meta['domain']: {
                "dev_name": response.meta['dev_name'],
                "filled_external_source": response.meta['filled_external_source'],
                "sub_status": sub_status,
                "name": name,
                "country": country,
                "records": records,
            }}


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "data/spidernest_data.json": {
                "format": "json",
                "overwrite": True,
                'encoding': 'utf8',
            },
        },
    })
    process.crawl(SpiderNest)
    process.start()
