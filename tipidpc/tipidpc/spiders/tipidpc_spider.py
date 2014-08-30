from urlparse import urljoin
from urllib import quote_plus

from scrapy.spider import Spider
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.loader.processor import MapCompose

from tipidpc.items import TipidPCItemLoader
from tipidpc.processors import ParseDate


class TipidPC(Spider):

    name = 'tipidpc'
    allowed_domains = ['tipidpc.com']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(TipidPC, self).__init__(*args, **kwargs)

        self.username = kwargs.get('username')
        self.search = kwargs.get('search')
        self.price = float(kwargs.get('expected_price', 0))
        self.price_tolerance = float(kwargs.get('price_tolerance', 20))

        assert not (self.username and self.search), 'Enter a Username OR a Search query.'

        if self.username:
            self.start_urls.append(
                'http://www.tipidpc.com/useritems.php?username=%s'
                % self.username
            )

        if self.search:
            self.start_urls.append(
                'http://www.tipidpc.com/itemsearch.php?sec=s&namekeys="%s"'
                % quote_plus(self.search)
            )

    def parse(self, response):
        sel = Selector(response)

        if self.search:
            for url in sel.xpath('//select[@id="selectfield"]/option[position()<26]/@value').extract():
                yield Request(
                    url=urljoin(response.url, url),
                    callback=self.parse_search_results
                )
        else:
            for url in sel.xpath('//table[@class="itemlist"]/tbody/tr/td/a/@href').extract():
                yield Request(
                    url=urljoin(response.url, url),
                    callback=self.parse_item_page
                )

    def parse_search_results(self, response):
        sel = Selector(response)

        for url in sel.xpath('//h2/a/@href').extract():
            yield Request(
                url=urljoin(response.url, url),
                callback=self.parse_item_page
            )

    def parse_item_page(self, response):
        sel = Selector(response)
        loader = TipidPCItemLoader(selector=sel)

        loader.add_xpath(
            'price', '//h2[@class="itemprice"]/text()', re=r'PHP\s(\d+\.\d{2})'
        )
        loader.add_xpath('name', '//h1[@class="itemname"]/text()')
        loader.add_xpath(
            'date_posted',
            '//p[@class="itemmeta"]/text()[position()=2 or position()=3]',
            ParseDate(),
            re=r'on\s(.*\s[A|P]M)'
        )
        loader.add_xpath('description', '//div[@class="itemdesc"]')
        loader.add_value('item_id', response.url, re=r'iid=(\d+)')
        loader.add_value('source_url', response.url)

        yield loader.load_item()
