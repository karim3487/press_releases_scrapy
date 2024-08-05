import scrapy

from press_releases.db import Session
from press_releases.items import PressReleasesItem
from press_releases.utils import str_to_datetime, news_exists


class MchsSpider(scrapy.Spider):
    name = "mchs"
    allowed_domains = ["mchs.gov.kg"]
    start_urls = ["https://www.mchs.gov.kg/ru/news/"]

    def parse(self, response):
        press_releases = response.css("div.newsCard-wrap")
        for press_release in press_releases:
            detail_page_link = press_release.css("a.newsCard__title::attr(href)").get()
            if detail_page_link:
                if not news_exists(Session(), detail_page_link):
                    yield response.follow(detail_page_link, self.parse_detail)

    def parse_detail(self, response):
        item = PressReleasesItem()
        item["title"] = response.css("h1.news-title::text").get()
        item["text"] = "\n".join(
            text.strip() for text in response.css("div.col-xl-10 p::text").getall()[3:]
        ).strip()
        item["date_published"] = str_to_datetime(
            response.css("p.me-2::text").get(), "%d.%m.%Y %H:%M"
        )
        item["link_to_record"] = response.url
        yield item
