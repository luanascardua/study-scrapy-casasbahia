# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CasasbahiaPipeline:
    def process_item(self, item, spider):
        print(f'Pipeline: {item["title"][0]}')
        return item
