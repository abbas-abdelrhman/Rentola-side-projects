import json

import scrapy

from scrapy.crawler import CrawlerProcess

new_doms = ['accessasset.appfolio.com', 'actionapartments.appfolio.com', 'adanalian.com', 'apexidx.com',
            'apmlease.com', 'app.tenantturner.com', 'arrowheadhousing.appfolio.com', 'beverlyrealty.com',
            'blueoakchico.com', 'borelli.appfolio.com', 'buffalocityliving.managebuilding.com', 'calwestern.com',
            'calwestrents.com', 'coldwellbankerhomes.com', 'createbecomeimagine.com', 'eaglepropertymgmt.appfolio.com',
            'firstraterentals.net', 'freerentalsite.com', 'gaulerrealty.com', 'goldfishproperties.appfolio.com',
            'greenpropertyllc.appfolio.com', 'havenrents.com', 'hignellrentals.com', 'homes.vipteamrealestate.com',
            'housesforrent.ws', 'howardmanagement.com', 'hpmla.com', 'hpmrentals.com', 'inclineattahoe.appfolio.com',
            'ingeniousassetgroup.appfolio.com', 'keychainrealestate.com.au', 'landlordspm.com',
            'listings.gatewayarmsrealty.com', 'listings.heropm.com', 'mabrymgmt.com', 'managementone.com',
            'mcmprop.com', 'meritgroupassociates.com', 'meritrealestate.com', 'mesaproperties.net', 'mpghousing.com',
            'normandieapts.com', 'northcounty.appfolio.com', 'nycityapartment.com', 'openforhomes.com',
            'performancepm.appfolio.com', 'properties.hantangrealty.com', 're.cr', 'rentinginlosangeles.com',
            'rentpms.com', 'sdlrealestate.com', 'sdppm.appfolio.com', 'search.countryhouserealty.net',
            'sgpmrentals.com', 'showmojo.com', 'smartlarealty.com', 'smithhanten.com', 'tahoenorthrentals.appfolio.com',
            'tdipropertiesinc.com', 'teamforss.com', 'thomasrealtors.appfolio.com', 'tiaoproperties.com',
            'tlcre.appfolio.com', 'valleyoak.appfolio.com', 'vippropertyinc.com', 'willowsrentals.com', 'ziprent.com']


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
        yield scrapy.Request(
            url=f"https://c.findboliger.dk/spider_details?utf8=%E2%9C%93&per_page=50&order=&spider_detail%5Bcountry%5D=united_states&spider_detail%5Bstatus%5D=&spider_detail%5Bcategory%5D=&spider_detail%5Bassigned%5D=&spider_detail%5Boperator%5D=&spider_detail%5Blisting_count%5D=&spider_detail%5Bteam_id%5D=&spider_detail%5Bdeveloped_by_id%5D=&spider_detail%5Bapproval_status%5D=&spider_detail%5Bflag_status%5D=&spider_detail%5Bspider_tags%5D=&spider_detail%5Bwith_errors%5D=0&spider_detail%5Bname%5D=&spider_detail%5Bdomain%5D=&commit=Search",
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse,
        )

    # 2. SCRAPING level 2
    def parse(self, response, **kwargs):
        for item in response.xpath('//table[@class="table"]/tbody//tr'):
            domain = item.xpath('./td[2]/a/text()').get()
            status = item.xpath('./td[7]//text()').get()
            live_listings = item.xpath('./td[6]//text()').get()
            if domain in new_doms:
                yield {
                    "domain": domain,
                    "status": status,
                    "live_listings": live_listings
                }

        next_page = response.xpath('//ul[@class="pagination"]/li/a[contains(.,"Next")]/@href').get()
        yield scrapy.Request(
            url="https://c.findboliger.dk{}".format(next_page),
            callback=self.parse,
            cookies=self.cookies,
            headers=self.headers,
        )


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "/home/abbas/PycharmProjects/QA-Automation/data/USA/active-domains.csv": {
                "format": "csv",
                "overwrite": True,
                'encoding': 'utf8',
            },
            "/home/abbas/PycharmProjects/QA-Automation/data/USA/active-domains.json": {
                "format": "json",
                "overwrite": True,
                'encoding': 'utf8',
            },

        },
    })
    process.crawl(SpiderNest)
    process.start()
