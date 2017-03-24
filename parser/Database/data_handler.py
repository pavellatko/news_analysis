from Database import News, Users, ReadNews
from Database import connect_db
from NewsFetcher.parse import NewsParser


class NewsAdder:
    def __init__(self):
        self.session = connect_db()

    def add(self, id):
        parser = NewsParser(id)
        if not parser.success:
            return False
        try:
            date = parser.get_date()
            header = parser.get_header()
            text = parser.get_text()
        except Exception:
            return False
        news_entry = News(id=id, date=date, header=header, text=text)
        self.session.add(news_entry)
        self.session.commit()
        return True


class UserAdder:
    def __init__(self):
        self.session = connect_db()

    def add_user(self, id):
        ev = self.session.query(Users.id).filter(Users.id==id).count()
        if not ev:
            new_user = Users(id=id)
            self.session.add(new_user)
            self.session.commit()

    def add_read_entry(self, news_id, user_id):
        read_entry = ReadNews(user_id=user_id, news_id=news_id)
        self.session.add(read_entry)
        self.session.commit()


class NewsLoader:
    def __init__(self):
        self.session = connect_db()

    def unread_news(self, id, count):
        subquery = self.session.query(ReadNews.news_id).filter(ReadNews.user_id==id)
        query = self.session.query(News.id, News.date, News.header).\
            filter(News.id.notin_(subquery)).order_by(News.id.desc()).limit(count)

        return self.session.execute(query).fetchall()

    def get_news_full_text(self, id):
        query = self.session.query(News.date, News.header, News.text).filter(News.id==id).one()
        return '\n\n'.join(query)

    def latest_news(self):
        return self.session.query(News.id).order_by(News.id.desc()).first()[0]
