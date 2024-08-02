import locale
from datetime import datetime

from sqlalchemy.orm import Session

from press_releases.models import Source, Record

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


def str_to_datetime(str_datetime: str, datetime_format: str) -> datetime:
    # datetime_format = "%d.%m.%Y %H:%M"
    return datetime.strptime(str_datetime, datetime_format)


def news_exists(session: Session, url: str) -> bool:
    return session.query(Record).filter_by(link_to_record=url).first() is not None
