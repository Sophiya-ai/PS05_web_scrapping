import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    # start_urls - это та ссылка, от которой начинается парсинг
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
        # оператор "yield" помогает обрабатывать одно отдельное действие
        # С его помощью мы можем управлять потоком выполнения,
        # останавливать и возобновлять работу парсера (С другими операторами мы такого делать не можем)
            yield{
                'name' : divan.css('div.lsooF span::text').get(),
                'price' : divan.css('div.pY3d2 span::text').get(),
                'url' : divan.css('a').attrib['href']
            }
