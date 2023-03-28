import scrapy
import re
from ..items import IndividualsSpidersItem
from scrapy.loader import ItemLoader

sites_cookies = {
    'rentola.com': {
        "first_attribution": "Z1BQZnVWQS96V1B1Q2FyZVVhQUdYUlZDZDNmd2lMaFZoRjNCOFdJUU8xa2lQOVRKYWtzTG9XcWtPdnY1MnRPSFpzWVJSOVk3dkJ2UDJMeFJhSlI3dnVDc1FyK2MzaStmYTZWT3VRR001MVJpM3FMOVZVYmlRUlZKSldQMW9oWk5ZU05BYUljeCtnNXI5clltQlVJUTl6aTlmb094a1FGbGJzVitkWm9Od0RmSVVwUU5EdXozVHJKWXVLdXNRdFJEbHNOZFZ1bjV2MWwrMzVYU0NzdlJEQT09LS05eDNTbTVTYStzVlEwQnVGV1FQL1pRPT0=--31d884c5001f585a646b469e914ea66846c90bdd",
        "CookieInformationConsent": """{"website_uuid":"a9495f36-2626-44db-919e-12bb44163052","timestamp":"2023-01-02T20:00:26.735Z","consent_url":"https://rentola.com/listings/dublin-road-limerick-limerick-city-limerick-spotmycrib-0f8dd2","consent_website":"rentola.com","consent_domain":"rentola.com","user_uid":"17f249cd-e810-41d3-942e-4b42528c81a4","consents_approved":["cookie_cat_necessary","cookie_cat_functional","cookie_cat_statistic","cookie_cat_marketing","cookie_cat_unclassified"],"consents_denied":[],"user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}""",
        "last_attribution": "YVRzYmJINm9RK1NLa0VUODhrTDg1WXc1T0xpd0lXWmc5eExoNUhTSFBDTHdjVkJwdzkwQnBKcUZMOGVjMkUxM2ZQUmhrdzQ5YXZYNHB1eEU2K2NGRDgxUnZIREtpczFiczNFZzdpYnlQMjVxU0NUc3FlVE1aVjlXdzNsb29IZUltbWJrS1M3aVErRU5XQ2JNbW44L3VHSlJvd3ExTysvT0RTOFF6MTMwY3Vqc3RwMVNhQ1NBSUJ5VXdnMy9XWFNHY0VKb2JGN0lBbGt1dzBHeVp2dEZJQT09LS1MaWJFU3FoSFQxMkNhd0VMenBoM1V3PT0=--0c467cb1f93a981617d05b209f63ac3fb815d289",
        "_rentola_session": "dVQvZUQ1UHI1ZWlzdkdtbUdWUW0xK1FFQUEwb2g5VjFJUDdsUTVzYXFQUmJjWTA5YWd3R1hVU2FhR1RZa2ZoaG5YMElFdjhCYTVCK205RlNCTDlVZEpaZnM1ZHhmaHdsVEVKQlZJZEpzTDlKRkJJS3NxRUQ0NXhpQ3U4Rm5OY2hQWE8yOTNhOHlodnIzMFgzcU1JVlB5ZTc4QzFvWlltMDllalhpRlk4SEdKeXV0eERRYVNWUHNnRkZyd0ZSVjNySFhOREJWTFNnOXdNQiszVmlzS0tEdHZmOGo3blR3a2FJNnBEZEIvTGtrQWMzWjRSWkhqakx6Y2N6V3ZFNkxCSU9kNWVuc0U0UWtIOFp1VXdEdHVLQlE9PS0tck9xU1Z0Q0RBUmYrR0NDRGNkVDB1dz09--02f17b8dc8f87e900a3548717d2fba5c038c9b7d",
    },

    "findallrentals.com": {
        "first_attribution": "dVI4eG8yVG96QUMraHJGYUNMVjVRd2dFUy9SVmUzMW1kVU1wT2xaZDdiS2hsdjJWOVpmQTQxZVVad2RMTVBYanBiUHVtazVlSHcxTHU1T1U0dDF3dEdCWmdEbFo1Mm9vcTZTTjN4czQ1VldFd0F2SVBLUlFqNDBEc0tpdUdpNzI3NUV1azhMcmxmMFprTzMrNit5VjgwTXZzWmNMWG82SGlSeUcrZWc0UFQ2V3JLQzh1REgwWmhlbnRnNm9TNzJjWEovY2JnSFZVRW9NY0VRTmlMSTZaN2xYNTBmMS95K01ENGFENlBuc0twY0JVOVRhcjlxSHVmNmwxTjlqV3c1eS0tcjNXL0tzYkVZaTc4cVRkeHNTaFhydz09--a8fe5ee29c5cf8d2d8141cbf5f90be5ce654162c",
        "CookieInformationConsent": """{"website_uuid":"68bd052b-e037-4cb3-a53e-41ed3a77443e","timestamp":"2023-01-12T01:52:22.261Z","consent_url":"https://findallrentals.com/listings/gezellige-1-slpkwoning-binnen-de-grote-ring-immo-vanderveken-5f4190","consent_website":"findallrentals.com","consent_domain":"findallrentals.com","user_uid":"cdc4c884-0f75-4fc3-9614-f842ffc1de13","consents_approved":["cookie_cat_necessary","cookie_cat_functional","cookie_cat_statistic","cookie_cat_marketing","cookie_cat_unclassified"],"consents_denied":[],"user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}""",
        "search-agent-popup-closed": "1",
        "request_method": "POST",
        "last_attribution": "bUtFOUg0RFk0RUpSaUZneUVYSFhHNEJsTHE1cnlGenZUUytZam9kb3pXdmF0UkhIMDhrMkZUMjdFL3lHSjRoOXk4cVdWTlUzS3FmRCtST29mdEpnZUZRdmJRWVRrdS9ZT21tR0JvSTgxZ3RqOTRlTVBoNnJtbVIyTE5VYW1vbFVzc1RsdURKVFJjU1RBWTBHYVIzTUtUMUExdmhHMFYzVStEMTl2S0dUQnJPREtwVXBVTUZQajJ3YTRGSjBQckQ5VVp4N2ZvQ1lqc21FYnhERmxCMDlrUT09LS1Vb2JIemFIL1hTSXl5NnhIUWJFMHRBPT0=--ea6ed60ea52d713eefa429c2a06939b71dd9317f",
        "_rentola_session": "NkFheVhmM1BaRFc2YVUzc0pKbUJzbFB6Zy8xSVM4bUFuTEU0dFZjV3NmS1JMbU9sWVRrMWo3MmZlSjhVOVBkTlpNSmFWaEszTkZiUUlpSUU4UmZWV1FEbERXMFU5UFpWanhZUzVINWJSbUhTamtLaFNGN2pxbzhWUHpCQms3TnBVTFB4YTNJY3Z0dWRQQWhKM0FaY0ZwV2VXM1pTb0toNGprRkl0emJXUVJxTnBQRDFkTnBMQnlhWW9kWGZjdi9QNmN4VzlYY2FqbFRqSDdxVUkvT3lIMklTMVljNEJHT1gxQlYxUExtTGYxWkVNaGFOSlJVVUtYRkFGNE1UdHRCUy0tNWFrOExXRmhrVUtGSkNkbm8vbjJLdz09--1fb39fbf5b8b9e89f2f11d7a6e0c87911fd0dc1c""",

    },

    "rentwyre.com": {
        "cs_test_cookie": "1",
        "first_attribution": """eUpuVEpzcEtISzhPNDNZOFZDbEQ0RGhkSzNnTUdGclMxNHErWDdSWDRyY25BdE9tN3I1OXV1Z1kzNEE1THhjNWNXR3QrTVdWQkpmY1p3cnhkWm5BZ0RIVk5ETEZOTS9rU1dFQllVQWxkY21HQVdiZVQ5bUFyN0V3dDBkc1RaSnhpS2JGSjhwMDJybzdYNFRRbjZ5SUhaLzY5QVRXOEVyeXZxVElGRHpHTmNnUHUvN2J5TUpZMnRhcDN5MFhHMzk4OWE5dTBpVlBmb1NsQU9ueUhibmZZdz09LS1NbWxrMXZ2T2pNdkw3NVIrS3U3d2JRPT0=--fac4a2bb3818df5becaf784c89816da2e153664b""",
        "CookieInformationConsent": """{"website_uuid":"72a560c3-96d8-4a01-92fb-f4a457fd21a6","timestamp":"2023-01-10T10:51:39.955Z","consent_url":"https://rentwyre.com/listings/le-mare-coco-del-mar-amoblado-205187ppz-p114462-inmopanama-e42ff2","consent_website":"rentwyre.com","consent_domain":"rentwyre.com","user_uid":"95541f6b-901b-40d5-bf69-318cadfeef3a","consents_approved":["cookie_cat_necessary","cookie_cat_functional","cookie_cat_statistic","cookie_cat_marketing","cookie_cat_unclassified"],"consents_denied":[],"user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}""",
        "popup-visited": '1',
        "last_attribution": """TFYydTMyRytqenpzMTV0djI2TkxlNmFac3lHUkh3NU9RWFJ5ZkJPY3krVHlxa3MzVUFhWkV3NCtobnB5T1E4WU5EWWI1eHFCSlI5VEF1MmFvSDRjUnNaVXhZUWNUOE11OTdpWUI3MkdQdFo4bFY1b1BYVjJJZ2NINGVrTzJrZHJXcnhOUnBkaHpPVVZyQnRyQ0VTQkdvcEFKbmJOQWhZV0lCWFZvRkV3cE9Ra3BsTHp2WkFKZDh2N2M0QURJUU1UeFhyb1FxbHBKQitBdGJlL1pnc0dwZz09LS1ydFBtUHJRQjRHRGpwaHZ2RHdsMEVnPT0=--d1c2af835ce559a0df0f20a74d5df28c04cc786e""",
        "_rentola_session": """RnlybkFrUEFTSnpzeEE0SGtQNm5Tamd6U2o3Zy8xZUQvd0k2T3NlS1B4ZmFCZjhJSmhQUUlMQi96YjF0aGFLejBkZ1ptcXUwZGhXREJFOUQ0SCtoaGZyUmdJdFROalc0RG1OdTF3c1dZMGpxMTFxVlRKcmtib2tDOXpFYUJYTXltNHpQWUdDbEJCR0E4NSsvSnlnNGRJSEp5MEJhTVlZNlcxandHSUR2aCtKT3FWYm9vUk51V2F1aXFsMzhnV21OdFJ1NjFocEpiaitDbFVsZjZycmE4aFp0Y2xnMWlaYUFKVUx6UFR6dEdUTU4rZENnYmVYMVhid1VobFRHUWx5ODBMN200bndGdkFiWFBJNGV5d1liT1FFV2VFZ0kxY3U4VUFCMUVyYURxem5mR2RaamNXS3RMY1JyK1FscFZtRU9pZE9Kb0o4ZVRVUnduVHVQblB5SUR3PT0tLXA4cXJNcU5xMXMzOHUrcUVlbDFzYXc9PQ==--cd7654f610eafbca866f4fd7b2909965b03b9eb0""",

    }
}


class RentwyreComSpider(scrapy.Spider):
    name = "rentwyre_com"
    allowed_domains = ["rentwyre.com"]

    start_urls = [
        {
            "url": "https://rentwyre.com/for-rent?order=area_asc",
            "allowed_domains": "rentwyre.com"
        }

    ]

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }

    position = 1

    # 1. SCRAPING level 1
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url["url"],
                                 headers=self.headers,
                                 callback=self.parse,
                                 meta={'allowed_domains': url['allowed_domains']})

    # 2. SCRAPING level 2
    def parse(self, response, **kwargs):
        allowed_domains = response.meta['allowed_domains']
        for item in response.xpath('//div[@class="col-md-12"]/div/div'):
            prop_link = item.xpath('.//a[@class="see-more fake-btn"]/@href').get()
            prop_price = item.xpath('.//div[@class="rent fake-btn"]/b/text()').get()

            if prop_link:
                yield scrapy.Request(
                    url="https://{}{}".format(allowed_domains, prop_link),
                    callback=self.populate_item,
                    cookies=sites_cookies[allowed_domains],
                    meta={'prop_price': prop_price}
                )

        next_page = response.xpath("//div[@class='hidden pagination']/a[@class='next-page']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,
                                 callback=self.parse,
                                 headers=self.headers,
                                 cookies=sites_cookies[allowed_domains],
                                 meta={'allowed_domains': allowed_domains})

    # 3. SCRAPING level 3
    def populate_item(self, response):
        items = ItemLoader(item=IndividualsSpidersItem(), response=response)
        images = response.xpath("//div[@class='fotorama']//a/img/@src").getall()

        area = response.xpath('//div[@class="f-row"]/div[contains(.,"Area:")]/following::div[1]/text()').get()
        if area:
            area = int(extract_number_only(area))

        bedrooms = response.xpath('//div[@class="f-row"]/div[contains(.,"Bedrooms:")]/following::div[1]/text()').get()
        if bedrooms:
            bedrooms = int(extract_number_only(bedrooms))

        bathrooms = response.xpath('//div[@class="f-row"]/div[contains(.,"Bathrooms:")]/following::div[1]/text()').get()
        if bathrooms:
            bathrooms = int(extract_number_only(bathrooms))

        source_link = response.xpath('//ul[@class="list list-inline"]/li[contains(.,"Source:")]/a/@href').get()

        domain = None
        if source_link:
            domain = source_link.split('://')[-1].split('/')[0].replace('www.', '')

        items.add_value('rentola_link', response.url)
        items.add_value('source_link', source_link)
        items.add_value('domain', domain)
        items.add_value('prop_price', response.meta['prop_price'])
        items.add_value('area', area)
        items.add_value('bedrooms', bedrooms)
        items.add_value('bathrooms', bathrooms)
        items.add_value('images_length', len(images))

        items.add_value("position", self.position)
        self.position += 1
        yield items.load_item()


def extract_number_only(input_string, thousand_separator='.', scale_separator=','):
    input_string = str(input_string).replace(thousand_separator, "")
    input_string = input_string.replace(scale_separator, ".")

    numbers = re.findall(r'\d+(?:\.\d+)?', input_string)
    if numbers:
        return int(float(numbers[0]))
    else:
        return 0

# if __name__ == "__main__":
#     process = CrawlerProcess(settings={
#         "FEEDS": {
#             "data/downloaded_data.json": {
#                 "format": "json",
#                 "overwrite": True,
#                 'encoding': 'utf8',
#             },
#         },
#     })
#     process.crawl(QaAutomationSpider)
#     process.start()
