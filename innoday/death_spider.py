import scrapy


class TWDTranscriptSpider(scrapy.Spider):
    name = 'twd'
    start_urls = [
        'https://listofdeaths.fandom.com/wiki/The_Walking_Dead'
    ]

    def parse(self, response):
      for episode in response.xpath('//*[contains(@class, \'mw-parser-output\')]/h3'):
        yield {'text': episode.xpath('following-sibling::*[1]/li/descendant-or-self::*/text()').getall(), 'episode': episode.xpath('span/text()').get()}