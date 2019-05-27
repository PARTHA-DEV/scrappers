# -*- coding: utf-8 -*-
"""
Created on Mon May 13 07:41:31 2019

@author: Reets
"""

import scrapy
 

class FlipkartReviewsSpider(scrapy.Spider):
    name = 'flipkart_reviews'
    allowed_domains = ['flipkart.com']
    start_urls = ["https://www.flipkart.com/apple-iphone-8-plus-space-grey-64-gb/product-reviews/itmexrgvehtzhh9v?pid=MOBEXRGVQKBREZP8"]
    
    def parse(self, response):
        self.log('I just visited ' + response.url)
        for com in response.css('div.qwjRop'):
            item = {
                    'comments': com.css('div div::text').extract()
            }
            
            yield(item)

        next_page_url = response.css('a._3fVaIS::attr(href)').extract_first()
        
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            