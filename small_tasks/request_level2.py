import scrapy
import sys

from scrapy.crawler import CrawlerProcess


def read_links():
    links = []
    with open('../python_spiders/spiders/failed_req.txt', 'r') as file:
        for line in file.readlines():
            links.append(line.strip())

    return links


class RequestingLevel2(scrapy.Spider):
    name = "request_level2"
    start_urls = read_links()
    # allowed_domains = ["c.findboliger.dk"]
    all_links = []
    passed_links = []

    # 1. SCRAPING level 1
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,
                                 headers={
                                     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"},
                                 callback=self.parse)

    # 2. SCRAPING level 2
    def parse(self, response, **kwargs):
        self.passed_links.append(response.url)
        yield {
            'req_link': response.url
        }


def out_to_csv(items):
    with open("../python_spiders/spiders/console.txt", "w+") as out_file:
        for item in items:
            out_file.write(f"{item}\n")


process = CrawlerProcess(settings={
    "FEEDS": {
        "items2.json": {"format": "json"},
    },
})

process.crawl(RequestingLevel2)
process.start()


failed_links = set(read_links()) - set(RequestingLevel2.passed_links)
out_to_csv(failed_links)
