# -*- coding: utf-8 -*-
import scrapy
import json
from helper import decode_email
from hemnet_spider.items import HemnetSpiderItem


class HemnetStockholmSold12mSpider(scrapy.Spider):
    name = 'hemnet_stockholm_sold_12m'
    allowed_domains = ['www.hemnet.se']
    start_urls = [
        'https://www.hemnet.se/salda/bostader?location_ids%5B%5D=17744'
    ]

    def parse(self, response):
        for item in self.scrape(response):
            yield item

    def scrape(self, response):
        SOLD_RESULT_SELECTOR = '.sold-results__normal-hit'
        for listing in response.css(SOLD_RESULT_SELECTOR):
            item = HemnetSpiderItem()

            item['listing_url'] = listing.css('.item-link-container').xpath(
                '@href').get()
            listing_page = response.urljoin(item['listing_url'])
            request = scrapy.Request(listing_page,
                                     callback=self.get_listing_details)
            request.meta['item'] = item
            yield request
        next_page = response.css('.next_page').xpath('@href').get()
        """
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),
                                 callback=self.scrape)
        """

    def get_listing_details(self, response):
        item = response.meta['item']
        address = response.css(
            '.sold-property__address::text').getall()[-1].strip()
        raw_meta_data = response.css('.sold-property__metadata::text').getall()
        tmp = [
            a.strip().replace('\n', '') for a in raw_meta_data if a.strip()
        ][0]
        meta_data = [a.strip() for a in tmp.split('-')]
        item['address'] = address + ',' + meta_data[1]
        item['property_type'] = meta_data[0]
        item['sold_time'] = response.css(
            '.sold-property__metadata time').xpath('@datetime').get()

        map_data = json.loads(
            response.css('.sold-property__map').xpath(
                '@data-initial-data').get())
        item['coordinate'] = map_data.get('listing').get('coordinate')
        item['sold_price'] = response.css(
            '.sold-property__price-value::text').get().replace(u'\xa0',
                                                               '').strip()
        item['price_per_area'] = map_data.get('listing').get(
            'price_per_area').replace(u'\xa0', '').strip()
        item['fee'] = map_data.get('listing').get('fee')
        asked_price = map_data.get('listing').get('asked_price')
        if asked_price:
            item['asked_price'] = ''.join(
                [s for s in asked_price.replace(u'\xa0', '') if s.isdigit()])
        item['rooms'] = map_data.get('listing').get('rooms').replace(
            'rum', '').strip()
        item['living_space'] = map_data.get('listing').get('living_space')
        item['supplemental_area'] = map_data.get('listing').get(
            'supplemental_area')
        item['land_area'] = map_data.get('listing').get('land_area')
        item['broker_name'] = response.css(
            '.broker-contact-card__information strong::text').get().replace(
                '\n', '').strip()
        item['broker_agency'] = response.css(
            '.broker-link::text').get().replace('\n', '').strip()
        item['broker_phone'] = response.css(
            '.broker-contact__link::text').getall()[1].replace('\n', '')
        item['broker_email'] = decode_email(
            response.css('.__cf_email__').xpath('@data-cfemail').get())
        yield item
