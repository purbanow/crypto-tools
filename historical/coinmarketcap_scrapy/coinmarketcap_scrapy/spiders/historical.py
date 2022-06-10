import scrapy


class HistoricalSpider(scrapy.Spider):
    name = "historical"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        yield scrapy.Request(url='https://coinmarketcap.com/historical', callback=self.parse_historical, headers=self.headers)

    def parse_historical(self, response):
        historical_links = response.xpath('//a[contains(@class,"historical-link")]/@href').getall()
        historical_dates = list(map(lambda date: date[12:20], historical_links))
        print (historical_dates)
        yield {
            'historical_dates': historical_dates
        }