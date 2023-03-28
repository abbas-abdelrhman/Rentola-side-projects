# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndividualsSpidersItem(scrapy.Item):
    rentola_link = scrapy.Field()
    source_link = scrapy.Field()

    domain = scrapy.Field()

    prop_price = scrapy.Field()

    area = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()

    images_length = scrapy.Field()
    position = scrapy.Field()


