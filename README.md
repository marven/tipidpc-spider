Tipid PC Spider
=========

A spider made using Scrapy to scrape http://www.tipidpc.com

Usage
----

```sh
pip install scrapy, parsedatetime
cd tipidpc-spider/tipidpc/tipidpc
```

Scrape all items of a specific user.

```sh
scrapy crawl tipidpc -a username='PCHub'
```

Scrape all items of a search query. Mispriced items can be filtered out by specifying an expected price and the tolerence in percentage.

The following scrapes all items that come up by searching "U2312HM" and that have a price that is within 20% of 10000 (8000-12000).

```sh
scrapy crawl tipidpc -a search='U2312HM' -a expected_price='10000' -a price_tolerance='20' -o output.json -t json
```

Sample Item
----

```sh
  {
    "description": "<div class=\"itemdesc\">\n\n                Like brand new. No scratches. Warranty from pcHub till august 2013. Pics to follow. <br>\r\nRFS: upgrading to 2560x1400<br>\r\ntxt me at 09064610535\n      </div>",
    "item_ts": "2014-08-30 16:09:51.905938",
    "price": "8500.00",
    "source_url": "http://www.tipidpc.com/viewitem.php?iid=22825421",
    "item_id": "22825421",
    "date_posted": "2013-03-09",
    "name": "[SOLD]7-month-old Dell U2312hm monitor"
  }
```