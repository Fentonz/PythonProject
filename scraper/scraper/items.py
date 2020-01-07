# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    shop = scrapy.Field()
    pass
