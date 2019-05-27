# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class FlipkartReviewsItem(scrapy.Item):

    stars = scrapy.Field()
    comments = scrapy.Field()
