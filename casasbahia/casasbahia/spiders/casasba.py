import scrapy

from ..readlist import read_list


base_url = 'https://www.casasbahia.com.br/{}/b'


class CasasbaSpider(scrapy.Spider):
    name = 'casasba'

    found_items  = '//*[@class="SearchResults__Controls-sc-1j8xo2z-0 jrPaix"]/p/b/text()'
    texto = '/html/body/div[1]/div[2]/div/div/div[5]/div[2]/div/section/ul/li[5]/div/div[2]/a/div/div'
    rating = './/meta[@itemprop="ratingValue"]/@content'
    review = './/meta[@itemprop="reviewCount"]/@content'
    title  = './/h2[@class="ProductCard__Title-sc-2vuvzo-0 iBDOQj"]//text()'
    image  = './/img/@src'
   
    def start_requests(self):
        for self.item in read_list():
            yield scrapy.Request(base_url.format(self.item))

    def parse(self, response):
        for i in response.xpath('//li[@class="ProductCard__Wrapper-sc-2vuvzo-9 bERDot"]'):
            rating = i.xpath(self.rating).extract()
            review = i.xpath(self.review).extract()
            title  = i.xpath(self.title).getall()
            image  = i.xpath(self.image).getall()
    
            yield {
                'term':self.item,
                'found items':response.xpath(self.found_items).extract(),
                'title':title,
                'review':review,
                'rating':rating,
                'url':response.url,
                'image':image
            }
