import sqlite3

from base_repo import BaseRepository
from helper_config import get_db_path


class Book:

    def __init__(self, id, title, author, publish_year):
        self.id = id
        self.title = title
        self.author = author,
        self.publish_year = publish_year

class BookRepository(BaseRepository):

    def __init__(self):
        path = get_db_path ()
        super().__init__(f'{path}book.db')
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Book(book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, publish_year INTEGER);')

    def get_all_books(self):
        self._cursor.execute('select * from Book;')
        data = self._cursor.fetchall()
        return data

book1= BookRepository()
print(book1.get_all_books())



