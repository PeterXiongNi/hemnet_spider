# -*- coding: utf-8 -*-
import scrapy
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
        LISTING_SELECTOR = '.normal-results__hit'
        for listing in response.css(LISTING_SELECTOR):
            item = HemnetSpiderItem()

            item['url'] = listing.css('a').xpath('@href').get()
            listing_page = response.urljoin(item['url'])
            request = scrapy.Request(listing_page,
                                     callback=self.get_listing_details)
            request.meta['item'] = item
            yield request

    def get_listing_details(self, response):
        item = response.meta['item']
        info_names = response.css('.attribute strong::text').getall()
        info_values = response.css('.attribute small::text').getall()
        helper.extract_measurements(info_names, info_values, item)

        item['image_urls'] = response.css('.more').xpath('@href').getall()
        yield item
