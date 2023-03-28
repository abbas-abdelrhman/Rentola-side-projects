# -*- coding: utf-8 -*-
# V2.0

import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from scrapy.utils.project import get_project_settings


class SpidernestListingSpider(scrapy.Spider):
    name = "spidernest_listing"
    start_urls = [
        # 'https://c.findboliger.dk/listings?source=&status=active&query=',
        # "https://c.findboliger.dk/listings?source=123wonen_nl_PySpider_netherlands_nl&status=inactive&query="
        # "https://c.findboliger.dk/listings?source=123wonen_nl_PySpider_netherlands_nl&status=active&query="
        "https://c.findboliger.dk/listings?source=Immotop_PySpider_belgium&status=active&query="


    ]
    # allowed_domains = ["c.findboliger.dk"]

    all_links = []
    passed_links = []
    cookies = {
        "_spider_nest_session": "2tTUX%2BLRCjnePh3HKG7G8X8g7XexfWoH5D14qSbTAnFo8dnb%2BL%2FZyfW0JOnpIPRdgMKRZiKepjh%2B%2BFyhCNLVuJXZ6M4t19NPxJybqq48oPMftufYTnU9%2BHX3wXYqli%2B9dNtRnGtaI9ApmxrsdVkHGSJIe0qYclp5YgGnP3KmBknRcZ8kRESqoTqRBg%2FJWFyZoOvTd%2Boy6bvzKn%2FL4AokS3NjFIwEeNI%2Ba9GpVeYdfjepTXxa6Be4xOY82D8bbQvsOi4hfi2urxCFNYaA0TZAe24kOe1Rxa38vVmoisFmGOtV%2B5Zjt91P2rO8Kv%2BHTCX%2FvZkLbCDa4w0Qn7QllcCYfFy5i5gSQnEDwImIyn6Zv5fJLqYBFYuRBAEjyARpgLfqG0GsV7SbG36VlH20iIr3kyE4b1cfJsBnqMrRjIaniD1d9PgQRx88knXzGsPDreWp1C9iCpV9Q%2B5TXSOKv%2FxirCOigeYD7I%2BppvFBGwelwp2Pf%2Brez9B90I%2F6ZCh2KvP2NN3QL8jiwxCkYTAJbSAQi1Uah%2FJvqqzAHtVwZD%2BJDT4%2BE3%2FEubK6z1u3lcs8qPb6AFqcfIFXyuGwKog0VrJEK9Wc3H83zB%2FQHmkXGZBRiRIuLFIOirPBbKg8%2FbMDm3MnZCK8KH8SZl%2Bd7pt9JM6GcS9PL5dcNUNvinT%2B9ELyzDNU2Qdnhv4DxaRup5Z1UPBuepe6b4U2xIRveWzuUTIdu%2B%2B%2F7qeKMYf%2B2IeDa%2BK%2Fw%2B9i9qipWrrqUwLkNv7mDt81ERG91XXYnGdU%2F20ClerqCIQi6Zycsk2TQeLVrVaGF2hpuDhzGAKRetz9qMoJGPMLFC9tSpbSZvRzOjfCWuUr2BsSgjcPGfQx5qwS1cKwtTGu2f1CuPPjeObWilsCo21EOAgC%2F%2FNzm5lJukIV7vqsFu9fUYAI0t3NvvUt9QxuRYZPdP%2FgZc6zub3Q3A3w9vl8FacuW%2FAA6KKHVM6HJ4pWy%2FW67L23UWaagrsb--TezoMBoFGNM1B8Ca--Wmgx5ulL%2B3dwd6adRscf9g%3D%3D"}

    # 1. SCRAPING level 1
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.http.Request(url=url,
                                      cookies=self.cookies,
                                      callback=self.parse)

    # 2. SCRAPING level 2
    def parse(self, response, **kwargs):
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

        for row in response.xpath("//table[@class='table']//tr"):
            external_source = row.xpath('.//a[contains(.,"Source:")]//text()').get()
            external_link = row.xpath('.//a[contains(.,"Source:")]//@href').get()
            status = row.xpath('.//span//text()').get()
            price = row.xpath('.//div[@class="pull-right"]/strong/text()').get()
            title = row.xpath('./td/b//text()').get()
            print(title)

                # self.all_links.append(external_link)
                # yield scrapy.Request(
                #     url=external_link,
                #     # headers=headers,
                #     callback=self.populate_item,
                #     meta={"external_source": external_source}
                # )

        # next_page = response.xpath('//a[@rel="next"]/@href').get()
        # if next_page:
        #     # next_page_link = f"https://c.findboliger.dk{next_page}&query=&source=&status=active"
        #     next_page_link = f"https://c.findboliger.dk{next_page}"
        #     yield scrapy.http.Request(
        #         url=next_page_link,
        #         cookies=self.cookies,
        #         callback=self.parse)

    # 3. SCRAPING level 3
    def populate_item(self, response):

        external_source = response.meta['external_source']
        external_link = response.url

        self.passed_links.append(external_link)

        yield {
            "external_source": external_source,
            "external_link": external_link,
        }



configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

runner.crawl(SpidernestListingSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()  # the script will block here until all crawling jobs are finished



def out_to_csv(items):
    with open("../python_spiders/spiders/failed_req.txt", "w+") as out_file:
        for item in items:
            out_file.write(f"{item}\n")


failed_links = set(SpidernestListingSpider.all_links) - set(SpidernestListingSpider.passed_links)
out_to_csv(failed_links)
