# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HemnetSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listing_url = scrapy.Field()
    address = scrapy.Field()
    property_type = scrapy.Field()
    sold_time = scrapy.Field()
    coordinate = scrapy.Field()
    sold_price = scrapy.Field()
    price_per_area = scrapy.Field()
    fee = scrapy.Field()
    asked_price = scrapy.Field()
    rooms = scrapy.Field()
    living_space = scrapy.Field()
    supplemental_area = scrapy.Field()
    land_area = scrapy.Field()
    broker_name = scrapy.Field()
    broker_agency = scrapy.Field()
    broker_phone = scrapy.Field()
    broker_email = scrapy.Field()
