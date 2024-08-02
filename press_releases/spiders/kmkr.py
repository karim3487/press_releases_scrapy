import scrapy

from press_releases.items import PressReleasesItem
from press_releases.utils import news_exists, str_to_datetime

from press_releases.db import Session

months_dict = {
    "январь": "января",
    "февраль": "февраля",
    "март": "марта",
    "апрель": "апреля",
    "май": "мая",
    "июнь": "июня",
    "июль": "июля",
    "август": "августа",
    "сентябрь": "сентября",
    "октябрь": "октября",
    "ноябрь": "ноября",
    "декабрь": "декабря",
}


class KmkrSpider(scrapy.Spider):
    name = "kmkr"
    allowed_domains = ["www.gov.kg"]
    start_urls = ["https://www.gov.kg/ru/post/c/press"]

    def parse(self, response):
        press_releases = response.css(".section-item__title")
        for press_release in press_releases:
            detail_page_link = press_release.css("a::attr(href)").get()
            if detail_page_link:
                if not news_exists(Session(), detail_page_link):
                    yield response.follow(detail_page_link, self.parse_detail)

    def parse_detail(self, response):
        pr_date = response.css(
            ".medium-sm-black::text , .news-date-number::text"
        ).getall()
        pr_date[1] = months_dict[pr_date[1].lower()]
        pr_date = " ".join(pr_date)

        item = PressReleasesItem()
        item["title"] = response.css(".heavy-lg-black::text").get().strip()
        item["text"] = "\n".join(
            text.strip() for text in response.css("span::text").getall()
        ).strip()
        item["date_published"] = str_to_datetime(pr_date, "%d %B %Y")
        item["link_to_record"] = response.url
        yield item
