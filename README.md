# simpleCrawler
crawl exchange rate data with selenium and return json format

usage:
```
spyder = SEcrawler()
data = spyder.crawler('USD') # latest 20 pages from esubank website's data of USD to TWD
print(data) # JSON format

# other currencys for e.g. ['USD', 'CNY', 'AUD', 'EUR', 'HKD']
```
output:
```
{ "USD": { "2019-09-23": { "buy": "30.97", "sell": "31.07" }, ..., "2020-09-07": { "buy": "29.28", "sell": "29.38" } } } 
```
