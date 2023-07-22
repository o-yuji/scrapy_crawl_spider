# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst,MapCompose,Join

def strip_yen(el):
    if el:
        return el.replace('¥','').strip()
    return el

def strip_comma(el):
    if el:
        return el.replace(',','').strip()
    return el

def convert_int(el):
    if el:
        return int(el)
    return 0

def get_size(el):
    if el:
        return el.split('／')[0].replace('サイズ ','').replace('判','')
    return el

def page_size(el):
    if el:
        return el.split('／')[1].replace('ページ数 ','').replace('p','')
    return el

def get_isbn(el):
    if el:
        return el.replace('商品コード ','')
    return el

class BookItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(str.lstrip),
        output_processor = Join(' ')
    )
    author = scrapy.Field(
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(strip_yen,strip_comma,convert_int),
        output_processor = TakeFirst()
    )
    publisher = scrapy.Field(
        output_processor = TakeFirst()
    )
    size = scrapy.Field(
        input_processor = MapCompose(get_size),
        output_processor = TakeFirst()
    )
    page = scrapy.Field(
        input_processor = MapCompose(page_size,convert_int),
        output_processor = TakeFirst()
    )
    isbn = scrapy.Field(
        input_processor = MapCompose(get_isbn),
        output_processor = TakeFirst()
    )