import scrapy
import json


class CasasbaSpider(scrapy.Spider):
    name = 'casasba'
    page = 1
    name_categories = []

    base_url = 'https://prd-api-partner.viavarejo.com.br/api/search?resultsPerPage=20&terms=iphone&page={}&salesChannel=desktop&apiKey=casasbahia'
    start_urls = [base_url.format(1)]

    def parse(self, response):

        response_json = json.loads(response.body)
       
        for item in response_json.get('products', []):
            image = item.get('images')
            categories = item.get('categories')
            details = item.get('details')
            payment = item.get('installment')         
        
            for i in range(0, len(categories)):
                self.name_categories.append(categories[i]['name'])

            yield {
                'ID':item.get('id'),
                'status':item.get('status'),
                'name':item.get('name'),
                'image':image['default'],
                'price':item.get('price'),
                'categories':self.name_categories,
                'marca':details['marca'],
                'installment_qty':payment['count'],
                'installment_price':payment['price'],
                'url':item.get('url')
            }
            self.name_categories = []

        if response_json['pagination']['next']:
            self.page += 1
            yield scrapy.Request(self.base_url.format(self.page))
        