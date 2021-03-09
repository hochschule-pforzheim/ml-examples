import scrapy


class TWDTranscriptSpider(scrapy.Spider):
    name = 'twd'
    start_urls = [
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6481',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6482',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6483',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6484',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6485',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6916',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6917',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6918',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6919',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6920',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6921',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6922',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6923',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6925',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6926',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6927',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6928',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6929',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6930',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=7375',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6931',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6932',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6933',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6934',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6935',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6936',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6937',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6938',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6939',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6940',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=7376',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6941',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6942',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=6943',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=7377',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8820',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8831',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8839',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8845',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8857',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8945',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=8966',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=9058',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=9936',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=9949',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=9955',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=9980',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=10009',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=10113',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=10195',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=10442',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14161',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14233',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14285',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14331',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14375',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14421',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14468',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=14494',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=201&t=16450',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=16547',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=16643',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=16769',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=16895',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=17161',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=17444',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=17543',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=22973',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23186',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23349',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23472',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23641',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23784',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=23942',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=24045',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=25184',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=25518',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=25654',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=25792',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=25945',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=26151',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=26254',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=26392',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29207',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29246',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29379',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29526',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29678',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29864',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=29983',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=30103',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=30221',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=31003',
        'http://transcripts.foreverdreaming.org/viewtopic.php?f=15&t=31128'
    ]

    def parse(self, response):
      yield {'text': response.xpath('//*[contains(@class, \'postbody\')]/p/text()').getall(), 'episode': response.xpath('//*[contains(@class, \'boxheading\')]/h2/text()').get()}