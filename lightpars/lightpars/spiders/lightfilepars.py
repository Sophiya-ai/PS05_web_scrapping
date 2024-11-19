import scrapy


class LightfileparsSpider(scrapy.Spider):
    name = "lightfilepars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        all_light = response.css('div.LlPhw')
        for light in all_light:
            yield{
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                'url': light.css('a').attrib['href']
            }

