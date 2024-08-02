import scrapy

from press_releases.db import Session
from press_releases.items import PressReleasesItem
from press_releases.utils import news_exists, str_to_datetime


class NeskSpider(scrapy.Spider):
    name = "nesk"
    allowed_domains = ["nesk.kg"]
    start_urls = ["https://nesk.kg/ru/press-centr/novosti-i-press-relizy/"]

    def parse(self, response):
        press_releases = response.css("div.news_item")
        for press_release in press_releases:
            detail_page_link = press_release.css("a::attr(href)").get()
            if detail_page_link:
                if not news_exists(Session(), detail_page_link):
                    yield response.follow(detail_page_link, self.parse_detail)

    def parse_detail(self, response):
        item = PressReleasesItem()
        item["title"] = response.css("h3::text").get()
        item["text"] = "\n".join(response.css("p::text").getall())
        item["date_published"] = str_to_datetime(
            response.css("h5::text").get(), "%d %B %Y г."
        )
        item["link_to_record"] = response.url
        yield item
