from datetime import datetime

from scrapy.exceptions import DropItem


class AddItemTimestamp(object):
    def process_item(self, item, spider):
        item.setdefault('item_ts', str(datetime.now()))
        return item


class PriceFilter(object):
    def process_item(self, item, spider):
        if spider.price <= 0 or not spider.search:
            return item
        else:
            max_price = spider.price*(1+spider.price_tolerance/100)
            min_price = spider.price*(1-spider.price_tolerance/100)
            price = float(item['price'])
            
            if price > max_price or price < min_price:
                raise DropItem('Price too high/low.')
            else:
                return item
