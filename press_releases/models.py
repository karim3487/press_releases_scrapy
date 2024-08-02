from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    link = Column(Text, unique=True, nullable=False)

    records = relationship("Record", order_by="Record.id", back_populates="source")

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return f"<Source(name='{self.name}')>"


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(Text, nullable=False)
    date_published = Column(DateTime, nullable=False)
    source_id = Column(Integer, ForeignKey(Source.id))
    is_press_release = Column(Boolean, nullable=False, default=False)
    link_to_record = Column(String(255), nullable=False)

    source = relationship("Source", back_populates="records")

    def __init__(
        self, title, text, date_published, source_id, is_press_release, link_to_record
    ):
        self.title = title
        self.text = text
        self.date_published = date_published
        self.source_id = source_id
        self.is_press_release = is_press_release
        self.link_to_record = link_to_record

    def __repr__(self):
        return f"<Record(title='{self.title}', date_published='{self.date_published}')>"
