import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

class ComputerBooksSpider(CrawlSpider):
    name = "computer_books"
    allowed_domains = ["www.kinokuniya.co.jp"]
    start_urls = ["https://www.kinokuniya.co.jp/f/dsd-101001037028005-06-"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="heightLine-2"]/a'),
             callback="parse_item", follow=False),
        Rule(LinkExtractor(restrict_xpaths = '(//a[contains(text(),"次へ")])[1]'),
             follow=True)
        )

    def parse_item(self, response):
        logging.info(response.url)
