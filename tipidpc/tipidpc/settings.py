# Scrapy settings for tipidpc project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tipidpc'

SPIDER_MODULES = ['tipidpc.spiders']
NEWSPIDER_MODULE = 'tipidpc.spiders'

ITEM_PIPELINES = {
    'tipidpc.pipelines.AddItemTimestamp': 300,
    'tipidpc.pipelines.PriceFilter': 200
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tipidpc (+http://www.yourdomain.com)'
