# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from press_releases.db import Session
from press_releases.models import Source, Record


# useful for handling different item types with a single interface


class PressReleasesPipeline(object):
    def __init__(self):
        self.Session = Session()

    def insert_or_ignore_source(self, spider):
        source = self.Session.query(Source).filter_by(name=spider.name).first()
        if not source:
            source = Source(name=spider.name, link=spider.start_urls[0])
            self.Session.add(source)
            self.Session.commit()
        return source

    def process_item(self, item, spider):
        source = self.Session.query(Source).filter_by(name=spider.name).first()
        if not source:
            source = Source(name=spider.name, link=spider.start_urls[0])
            self.Session.add(source)
            self.Session.commit()

        record = Record(
            title=item["title"],
            text=item["text"],
            date_published=item["date_published"],
            source_id=source.id,
            is_press_release=True,
            link_to_record=item["link_to_record"],
        )

        self.Session.add(record)
        self.Session.commit()

        return item

    def close_spider(self, spider):
        self.Session.commit()
        self.Session.close()

    def open_spider(self, spider):
        self.Session = Session()
