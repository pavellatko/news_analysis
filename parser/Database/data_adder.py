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
        new_user = Users(id=id)
        self.session.add(new_user)
        self.session.commit()

    def add_read_entry(self, news_id, user_id):
        read_entry = ReadNews(user_id=user_id, news_id=news_id)
        self.session.add(read_entry)
        self.session.commit()
