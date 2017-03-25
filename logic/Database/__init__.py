from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_NAME

Base = declarative_base()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    date = Column(String(20), nullable=False)
    header = Column(String(500), nullable=False)
    text = Column(String(10000))


class Users(Base):
    __tablename__ = 'users'
    id = Column(String(50), primary_key=True)


class ReadNews(Base):
    __tablename__ = 'read_news'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey('users.id'))
    news_id = Column(Integer, ForeignKey('news.id'))
    news = relationship(News)
    user = relationship(Users)


engine = create_engine(DB_NAME)


def create_db():
    Base.metadata.create_all(engine)


def connect_db():
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()
