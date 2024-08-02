from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config_reader as cfg

from press_releases.models import Base

sqlite_uri = "sqlite:///press_rel.sqlite3"
postgresql_uri = f"postgresql://{cfg.USERNAME}:{cfg.PASSWORD}@{cfg.HOST}:{cfg.PORT}/{cfg.DB_NAME}"

engine = create_engine(postgresql_uri, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
