# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MlocatorItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
    upc = scrapy.Field()
    price = scrapy.Field()
    saleprice = scrapy.Field()
    retailer_key = scrapy.Field()
    instore = scrapy.Field()
    shiptostore = scrapy.Field()
    productstockstatus = scrapy.Field()
    gallery = scrapy.Field()
    features = scrapy.Field()
    brand = scrapy.Field()

    model = scrapy.Field()
    retailer_sku = scrapy.Field()
    currency = scrapy.Field()
    locale = scrapy.Field()
    categories = scrapy.Field()
    shippingphrase = scrapy.Field()
    membershiprequired = scrapy.Field()
