import scrapy
import re
from scrapy.crawler import CrawlerProcess
from ..items import ScraperItem


class Spider1A(scrapy.Spider):
    name = '1A'
    start_urls = [
        'https://www.1a.lv/datoru_komponentes_tikla_produkti/atmina_hdd_ssd/ram_flash_atminas',
        'https://www.1a.lv/datoru_komponentes_tikla_produkti/komponentes/procesori',
        'https://www.1a.lv/datoru_komponentes_tikla_produkti/komponentes/videokartes'
    ]

    def parse(self, response):
        items = ScraperItem()
        items['shop'] = self.name
        products = response.css('section.product')

        category = response.css('h1#smp-heading-tag::text').extract_first()
        if category == 'Operatīvā atmiņa (RAM)':
            items['category'] = 'RAM'
        elif category == 'Procesori':
            items['category'] = 'CPU'
        elif category == 'Video kartes':
            items['category'] = 'GPU'

        for product in products:
            id = product.css(
                'div.p-info a').css('::attr(pro_id)').extract_first()
            name = product.css('h3 a::text').extract_first()
            price = product.css(
                'div.price-v2::attr(data-sell-price-w-vat)').extract_first()

            items['id'] = id
            items['name'] = name
            items['price'] = price

            yield items

        next_page = response.css(
            'a.next.paging-link::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class SpiderDateks(scrapy.Spider):
    name = 'dateks'
    start_urls = [
        'https://www.dateks.lv/cenas/atmina-ram',
        'https://www.dateks.lv/cenas/procesori-amd',
        'https://www.dateks.lv/cenas/procesori-intel',
        'https://www.dateks.lv/cenas/videokartes'
    ]

    def parse(self, response):
        items = ScraperItem()
        items['shop'] = self.name
        products = response.css('div.prod')

        category = response.css('h1::text').extract_first()
        if category == 'Atmiņa (RAM)':
            items['category'] = 'RAM'
        elif category == 'Procesori (Intel)':
            items['category'] = 'CPU'
        elif category == 'Procesori (AMD)':
            items['category'] = 'CPU'
        elif category == 'Videokartes':
            items['category'] = 'GPU'
        else:
            items['category'] = 'unknown'

        for product in products:
            id = product.css(
                'div.top a').css('::attr(data-id)').extract_first()
            name = product.css('div.name::attr(title)').extract_first()
            price = product.css(
                'div.price::text').extract_first()

            # get rid of jiggerish
            price = re.sub("€", "", price)
            price = re.sub("\xa0", "", price)
            price = re.sub(" ", "", price)  # this is not normal whitespace
            price = re.sub(",", ".", price)

            items['id'] = id
            items['name'] = name
            items['price'] = price

            yield items

        next_page = response.css(
            'div.pages div.list a.prevnext::attr(href)')[-1].extract()  # we still rely on scrappy to not start from the beginning- that is not good
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class Spider220(scrapy.Spider):
    name = '220'
    start_urls = [
        'https://220.lv/lv/datortehnika/datoru-komponentes/operativa-atmina-ram',
        'https://220.lv/lv/datortehnika/datoru-komponentes/procesori-cpu',
        'https://220.lv/lv/datortehnika/datoru-komponentes/videokartes-gpu'
    ]

    def parse(self, response):
        items = ScraperItem()
        items['shop'] = self.name
        products = response.css('div.product-list-item')

        category = response.css('h1::text').extract_first()
        if category == 'Operatīvā atmiņa (RAM)':
            items['category'] = 'RAM'
        elif category == 'Procesori (CPU)':
            items['category'] = 'CPU'
        elif category == 'Videokartes (GPU)':
            items['category'] = 'GPU'

        for product in products:
            id = product.css('::attr(id)').extract_first()
            name = product.css('img::attr(alt)').extract_first()
            price = product.css('span.price.notranslate::text').extract_first()

            # get rid of jiggerish
            price = re.sub("€", "", price)
            price = re.sub(",", ".", price)
            price = re.sub(" ", "", price)
            price = re.sub("\n", "", price)

            items['id'] = id
            items['name'] = name
            items['price'] = price

            yield items

        next_page = response.css(
            'link[rel="next"]::attr(href)').extract_first()  # we still rely on scrappy to not start from the beginning- that is not good
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
