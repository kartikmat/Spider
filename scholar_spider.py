#!/bin/user/python
import scrapy
class ScholarSpider(scrapy.Spider):
    name = "scholar"
    start_urls = [
        'https://scholar.google.co.in/scholar?hl=en&q=goal+revision&oq=',
    ]

    def parse(self, response):
        for gs_ri in response.css('div.gs_ri'):
            yield {
                'LongLine': quote.css('div.gs_a::text').extract(),
             
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

