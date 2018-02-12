import scrapy

from tutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuotesItem()

        for quote in response.css('div.quote'):
            quote_item["text"] = quote.css('span.text::text').extract_first()
            quote_item["author"] = quote.css(
                    'small.author::text').extract_first(),
            quote_item["tags"] = quote.css('div.tags a.tag::text').extract()

            yield quote_item

            next_page = response.css(
                'li.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)