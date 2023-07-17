import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ComputerBooksSpider(CrawlSpider):
    name = "computer_books"
    allowed_domains = ["www.kinokuniya.co.jp"]
    start_urls = ["https://www.kinokuniya.co.jp/f/dsd-101001037028005-06-"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
