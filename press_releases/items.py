# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PressReleasesItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    date_published = scrapy.Field()
    link_to_record = scrapy.Field()
