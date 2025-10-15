# models.py

from datetime import datetime, timezone
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app

Base = declarative_base()

class Share(Base):
    __tablename__ = 'share'

    id = Column(Integer, primary_key=True)
    key = Column(String(8), unique=True, nullable=False)
    code = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Share id={self.id} key={self.key} date={self.date}>"


def get_session():
    engine = create_engine(current_app.config['POSTGRES_URL'])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
