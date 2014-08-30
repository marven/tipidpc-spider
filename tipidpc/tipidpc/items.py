from scrapy.item import Item, Field
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Identity, TakeFirst


class TipidPCItem(Item):
    name = Field()
    price = Field()
    date_posted = Field()
    description = Field()
    item_id = Field()
    source_url = Field()
    item_ts = Field()


class TipidPCItemLoader(ItemLoader):
    default_item_class = TipidPCItem
    default_input_processor = Identity()
    default_output_processor = TakeFirst()