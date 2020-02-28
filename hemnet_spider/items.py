# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HemnetSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    property_type = scrapy.Field()
    # TODO: check for proper name
    number_of_rooms = scrapy.Field()
    living_area = scrapy.Field()
    has_balcony = scrapy.Field()
    year_built = scrapy.Field()
    association = scrapy.Field()
    monthly_charge = scrapy.Field()
    price_per_squaremeter = scrapy.Field()
    description = scrapy.Field()
    start_price = scrapy.Field()
    address = scrapy.Field()
    # TODO: add pictures in stage 2
    # pictures = scrapy.Field()
    address = scrapy.Field()
    broker_name = scrapy.Field()
    broker_phone_number = scrapy.Field()
    broker_email_address = scrapy.Field()
